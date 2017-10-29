package com.itechhub.datawizards.smartcityai.activities;

import android.content.Intent;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.TabLayout;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.view.View;

import com.itechhub.datawizards.smartcityai.R;
import com.itechhub.datawizards.smartcityai.adapters.StatusAdapterVacancies;
import com.itechhub.datawizards.smartcityai.models.User;

public class Vacancies extends AppCompatActivity {
    private ViewPager pager;
    private StatusAdapterVacancies adapter;
    FloatingActionButton fab;
    private User _user;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.vacancies);
        try {
            _user = (User) getIntent().getSerializableExtra("_user");
            setTitle(_user.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
        initialize();
        Toolbar toolbar = findViewById(R.id.my_toolbar_vacancies);
        setSupportActionBar(toolbar);

        pager = findViewById(R.id.view_pager_vacancies);
        adapter = new StatusAdapterVacancies(getSupportFragmentManager(), Vacancies.this);
        pager.setAdapter(adapter);
        TabLayout tabLayout = findViewById(R.id.tabs_layout_vacancy);
        tabLayout.setupWithViewPager(pager);
        pager.setCurrentItem(0);
    }

    void initialize() {

        fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), ReportFault.class);
                intent.putExtra("_user",_user);
                startActivity(intent);
                finish();
            }
        });
    }

    @Override
    public void onBackPressed() {
        startActivity(new Intent(getBaseContext(), Login.class));
        finish();
    }
}
