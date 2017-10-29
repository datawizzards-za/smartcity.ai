package com.itechhub.datawizards.smartcityai.activities;

import android.animation.Animator;
import android.content.Intent;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.TabLayout;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.LinearLayout;
import android.widget.ListView;

import com.itechhub.datawizards.smartcityai.R;
import com.itechhub.datawizards.smartcityai.adapters.StatusAdapter;

import java.util.ArrayList;

public class Home extends AppCompatActivity implements View.OnClickListener {
    private ViewPager pager;
    private StatusAdapter adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.home);
        Toolbar toolbar = findViewById(R.id.my_toolbar);
        setSupportActionBar(toolbar);

        pager = findViewById(R.id.view_pager);
        adapter = new StatusAdapter(getSupportFragmentManager(),Home.this);
        pager.setAdapter(adapter);
        TabLayout tabLayout = findViewById(R.id.tabs_layout);
        tabLayout.setupWithViewPager(pager);
        pager.setCurrentItem(0);
    }

    @Override
    public void onBackPressed() {
        startActivity(new Intent(getBaseContext(),Login.class));
        finish();
    }

    @Override
    public void onClick(View view) {

    }
}
