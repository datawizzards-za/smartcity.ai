package com.itechhub.datawizards.smartcityai.fragments;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.itechhub.datawizards.smartcityai.R;

public class Recommended_Vacancies extends Fragment {

    public Recommended_Vacancies() {
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.recommended__vacancies, container, false);

        return view;
    }
}
