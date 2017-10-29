package com.itechhub.datawizards.smartcityai.activities;

import android.content.Intent;
import android.location.Address;
import android.location.Location;
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

import java.io.IOException;
import java.util.ArrayList;

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
    public void postData() {
        // Create a new HttpClient and Post Header
        HttpClient httpclient = new DefaultHttpClient();
        HttpPost httppost = new HttpPost("http://www.yoursite.com/script.php");

        try {
            // Add your data
            List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(2);
            nameValuePairs.add(new BasicNameValuePair("id", "12345"));
            nameValuePairs.add(new BasicNameValuePair("stringdata", "Hi"));
            httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs));

            // Execute HTTP Post Request
            HttpResponse response = httpclient.execute(httppost);

        } catch (ClientProtocolException e) {
            // TODO Auto-generated catch block
        } catch (IOException e) {
            // TODO Auto-generated catch block
        }
    }
}
