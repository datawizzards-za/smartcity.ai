package com.itechhub.datawizards.smartcityai.activities;

import android.content.Intent;
import android.location.Address;
import android.location.Location;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat.OnRequestPermissionsResultCallback;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient.ConnectionCallbacks;
import com.google.android.gms.common.api.GoogleApiClient.OnConnectionFailedListener;
import com.itechhub.datawizards.smartcityai.R;
import com.itechhub.datawizards.smartcityai.models.Address_;
import com.itechhub.datawizards.smartcityai.models.Fault;
import com.itechhub.datawizards.smartcityai.models.LocationUtil.LocationHelper;
import com.itechhub.datawizards.smartcityai.models.User;

import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Map;

import butterknife.BindView;
import butterknife.ButterKnife;

public class ReportFault extends AppCompatActivity implements ConnectionCallbacks,
        OnConnectionFailedListener, OnRequestPermissionsResultCallback{


    @BindView(R.id.btnLocation)
    Button btnProceed;
    @BindView(R.id.btnSubmitFault)
    Button btnSubmitFault;
    @BindView(R.id.etDescription)
    EditText etDescription;
    @BindView(R.id.etLocation)
    TextView etLocation;
    @BindView(R.id.spFaultName)
    Spinner spFaultName;

    private Location mLastLocation;
    private String currentLocation;
    private Address_ _address;

    double latitude;
    double longitude;
    User _user;
    LocationHelper locationHelper;
    ArrayList<String> stringArrayList = new ArrayList<>();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.fault);
        ButterKnife.bind(this);
        addElements();
        _user = (User) getIntent().getSerializableExtra("_user");
        locationHelper = new LocationHelper(this);
        locationHelper.checkpermission();

        ArrayAdapter<String> dataAdapter = new ArrayAdapter<>(this,
                android.R.layout.simple_spinner_item, stringArrayList);
        dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spFaultName.setAdapter(dataAdapter);
        //spFaultName.setOnItemClickListener(this);

        btnProceed.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                mLastLocation = locationHelper.getLocation();

                if (mLastLocation != null) {
                    latitude = mLastLocation.getLatitude();
                    longitude = mLastLocation.getLongitude();
                    getAddress();

                } else {

                    if (btnProceed.isEnabled())
                        btnProceed.setEnabled(false);
                    showToast("Couldn't get the location. Make sure location is enabled on the device");
                }
            }
        });
        btnSubmitFault.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(TextUtils.isEmpty(etDescription.getText())){
                    etDescription.setError("Required.");
                }else {
                    //String name, String description, User user, Address_ address
                    String text = spFaultName.getSelectedItem().toString();
                    Fault fault = new Fault(text,etDescription.getText().toString(),_user,_address);
                }
            }
        });
        // check availability of play services
        if (locationHelper.checkPlayServices()) {

            // Building the GoogleApi client
            locationHelper.buildGoogleApiClient();
        }

    }
void addElements(){
        stringArrayList.add("Sewage");
        stringArrayList.add("Traffic Lights");
        stringArrayList.add("Street Lights");
        stringArrayList.add("Main Wholes");
}

    public void getAddress() {
        Address locationAddress;

        locationAddress = locationHelper.getAddress(latitude, longitude);
        System.out.println("latitude      " + latitude);
        System.out.println("longitude      " + longitude);
        if (locationAddress != null) {

            String address = locationAddress.getAddressLine(0);
            String address1 = locationAddress.getAddressLine(1);
            String city = locationAddress.getLocality();
            String state = locationAddress.getAdminArea();
            String country = locationAddress.getCountryName();
            String postalCode = locationAddress.getPostalCode();

            String[] temp = address.split(",");

            String coordinates = latitude+","+longitude;
            _address = new Address_(temp[0],temp[1],city,state,postalCode,coordinates);

            if (!TextUtils.isEmpty(address)) {
                currentLocation = address;

                if (!TextUtils.isEmpty(address1))
                    currentLocation += "\n" + address1;

                if (!TextUtils.isEmpty(city)) {
                    currentLocation += "\n" + city;

                    if (!TextUtils.isEmpty(postalCode))
                        currentLocation += " - " + postalCode;
                } else {
                    if (!TextUtils.isEmpty(postalCode))
                        currentLocation += "\n" + postalCode;
                }

                if (!TextUtils.isEmpty(state))
                    currentLocation += "\n" + state;

                if (!TextUtils.isEmpty(country))
                    currentLocation += "\n" + country;
                etLocation.setText(address);
                showToast(currentLocation);
                btnProceed.setVisibility(View.GONE);
                btnSubmitFault.setVisibility(View.VISIBLE);
            }
        } else
            showToast("Something went wrong");
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        locationHelper.onActivityResult(requestCode, resultCode, data);
    }


    @Override
    protected void onResume() {
        super.onResume();
        locationHelper.checkPlayServices();
    }

    /**
     * Google api callback methods
     */
    @Override
    public void onConnectionFailed(ConnectionResult result) {
        Log.i("Connection failed:", " ConnectionResult.getErrorCode() = "
                + result.getErrorCode());
    }

    @Override
    public void onConnected(Bundle arg0) {

        // Once connected with google api, get the location
        mLastLocation = locationHelper.getLocation();
    }

    @Override
    public void onConnectionSuspended(int arg0) {
        locationHelper.connectApiClient();
    }


    // Permission check functions
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {
        // redirects to utils
        locationHelper.onRequestPermissionsResult(requestCode, permissions, grantResults);
    }

    public void showToast(String message) {
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onBackPressed() {
        Intent intent = new Intent(getBaseContext(), Vacancies.class);
        getIntent().putExtra("_user",_user);
        startActivity(intent);
        finish();
    }
    public class PostData extends AsyncTask<String,String,String>{
        // This is the JSON body of the post
        JSONObject postData;

        // This is a constructor that allows you to pass in the JSON body
        public PostData(Map<String, String> postData) {
            if (postData != null) {
                this.postData = new JSONObject(postData);

            }
        }
        // This is a function that we are overriding from AsyncTask. It takes Strings as parameters because that is what we defined for the parameters of our async task
        @Override
        protected String doInBackground(String... strings) {
            URL url = null;
            HttpURLConnection con = null;
            try {
               url = new URL("http://simplifypay.herokuapp.com//charge.php");
                con = (HttpURLConnection) url.openConnection();
                //add reuqest header
                con.setRequestMethod("POST");
                con.setRequestProperty("User-Agent", "Mozilla/5.0");
                        con.setRequestProperty("Accept-Language", "en-US,en;q=0.5");

                String urlParameters = "simplifyToken="+"token.getId()"+"&amount=1000";

                // Send post request
                con.setDoOutput(true);
                DataOutputStream wr = new DataOutputStream(con.getOutputStream());
                wr.writeBytes(urlParameters);
                wr.flush();
                wr.close();

                int responseCode = con.getResponseCode();
                System.out.println("\nSending 'POST' request to URL : " + url);
                System.out.println("Post parameters : " + urlParameters);
                System.out.println("Response Code : " + responseCode);

                BufferedReader in = new BufferedReader(
                        new InputStreamReader(con.getInputStream()));
                String inputLine;
                StringBuffer response = new StringBuffer();

                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();
                //print result
                System.out.println(response.toString());
                //
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                con.disconnect();
            }
            return null;
        }
    }
}
