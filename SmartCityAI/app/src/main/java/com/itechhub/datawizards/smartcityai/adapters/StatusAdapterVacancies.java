package com.itechhub.datawizards.smartcityai.adapters;

import android.content.Context;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentStatePagerAdapter;

import com.itechhub.datawizards.smartcityai.R;
import com.itechhub.datawizards.smartcityai.fragments.All_Vacancies;
import com.itechhub.datawizards.smartcityai.fragments.Recommended_Vacancies;

public class StatusAdapterVacancies extends FragmentStatePagerAdapter {
    private Context context;

    public StatusAdapterVacancies(FragmentManager fm, Context context) {
        super(fm);
        this.context = context;
    }

    @Override
    public Fragment getItem(int position) {
        if (position == 0) {
            return new Recommended_Vacancies();
        } else {
            return new All_Vacancies();
        }
    }

    @Override
    public int getCount() {
        return 2;
    }

    @Override
    public CharSequence getPageTitle(int position) {
        if (position == 0) {
            return context.getResources().getString(R.string.title_recommended_vacancies);
        } else {
            return context.getResources().getString(R.string.title_vacancies);
        }
    }
}
