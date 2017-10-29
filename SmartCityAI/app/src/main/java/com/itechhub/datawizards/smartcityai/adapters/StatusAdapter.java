package com.itechhub.datawizards.smartcityai.adapters;

import android.content.Context;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentStatePagerAdapter;

import com.itechhub.datawizards.smartcityai.R;
import com.itechhub.datawizards.smartcityai.fragments.In_Progress_Citizen;
import com.itechhub.datawizards.smartcityai.fragments.New_Faults_Citizen;
import com.itechhub.datawizards.smartcityai.fragments.Pending_Citizen;

public class StatusAdapter extends FragmentStatePagerAdapter {
    private Context context;

    public StatusAdapter(FragmentManager fm, Context context) {
        super(fm);
        this.context = context;
    }

    @Override
    public Fragment getItem(int position) {
        if(position == 0){
            return new New_Faults_Citizen();
        }else if(position == 1){
            return new In_Progress_Citizen();
        }else{
            return new Pending_Citizen();
        }
    }

    @Override
    public int getCount() {
        return 3;
    }
    @Override
    public CharSequence getPageTitle(int position) {
        if (position == 0) {
            return context.getResources().getString(R.string.title_new_faults);
        } else if(position==1){
            return context.getResources().getString(R.string.title_in_progress);
        }else {
            return context.getResources().getString(R.string.title_pending);
        }
    }
}
