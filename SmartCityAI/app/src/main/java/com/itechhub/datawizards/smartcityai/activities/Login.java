package com.itechhub.datawizards.smartcityai.activities;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import com.itechhub.datawizards.smartcityai.R;
import com.itechhub.datawizards.smartcityai.models.User;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;

import butterknife.BindView;

public class Login extends AppCompatActivity {
    private ArrayList<User> users = new ArrayList<>();
    private EditText etUsername, etPassword;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login);
        initialize();
        Button btnCitizen = findViewById(R.id.citizen);
        Button btnEmployee = findViewById(R.id.employee);

        btnCitizen.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                new JSONTask().execute("http://192.168.8.106:8000/app/personal/ofentswe/");
            }
        });
        btnEmployee.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(getBaseContext(), Home.class));
                finish();
            }
        });
    }

    void initialize() {
        etUsername = findViewById(R.id.etUserName);
        etPassword = findViewById(R.id.etPassword);
    }

    private class JSONTask extends AsyncTask<String, String, String> implements AdapterView.OnItemClickListener {

        @Override
        protected String doInBackground(String... params) {
            BufferedReader reader = null;
            HttpURLConnection connection = null;
            try {
                URL url = new URL(params[0]);
                connection = (HttpURLConnection) url.openConnection();
                connection.connect();

                InputStream stream = connection.getInputStream();
                reader = new BufferedReader(new InputStreamReader(stream));
                StringBuffer buffer = new StringBuffer();
                String line;
                while ((line = reader.readLine()) != null) {
                    buffer.append(line);
                }
                String jsonObject = buffer.toString();
                String finalObject = "{" + '"' + "users" + '"' + ": " + jsonObject + "}";

                JSONObject jsonParent = new JSONObject(finalObject);
                JSONArray jsonArray = jsonParent.getJSONArray("users");

                for (int i = 0; i < jsonArray.length(); i++) {
                    JSONObject object = jsonArray.getJSONObject(i);
                    String name = object.getString("first_name");
                    String surname = object.getString("last_name");
                    String address = object.getString("email");
                    String username = object.getString("username");

                    System.out.println("name: "+ name+", Surname: "+surname+", address: "+address+", username: "+username);
                    users.add(new User(name, surname, address, username));
                }
                return buffer.toString();
            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            } catch (JSONException e) {
                e.printStackTrace();
            } finally {
                if (connection != null)
                    connection.disconnect();
                try {
                    if (reader != null)
                        reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return null;
        }

        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);
            if (validateInpuut()) {
                for (User user : users) {
                    if(user.getUsername().equals(etUsername.getText().toString())&&
                            user.getSurname().equals(etPassword.getText().toString())){
                        Toast.makeText(getBaseContext(),"Access granted",Toast.LENGTH_LONG).show();
                        Intent intent = new Intent(getBaseContext(),Vacancies.class);
                        intent.putExtra("_user",user);
                        startActivity(intent);
                        finish();
                    }
                }
            }
        }

        public boolean validateInpuut() {
            if (TextUtils.isEmpty(etUsername.getText())) {
                etUsername.setError("Required.");
                return false;
            } else {
                etUsername.setError(null);
            }
            if (TextUtils.isEmpty(etPassword.getText())) {
                etPassword.setError("Required.");
                return false;
            } else {
                etPassword.setError(null);
            }
            return true;
        }
        @Override
        public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {

        }
    }
}
