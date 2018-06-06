#include <iostream>
#include <vector>
#include <math.h>
#include <string>
#include <fstream>
#include "fisheye_files/IPM.h"
#include "fisheye_files/IPM.hpp"

using namespace cv;
using namespace std;

int main(int argc, char **argv)
{   
    Mat map1_center,map2_center;
    std::ifstream matcenter("fisheye_files/b.txt",std::ios::in);
    std::ifstream distcenter("fisheye_files/a.txt",std::ios::in);
    
    std::vector<double> a;
    std::vector<double> distCoeff_center;
    double num1 = 0.0;
    while (matcenter >> num1) 
    {
        a.push_back(num1);
    }
    double num2 = 0.0;
    while (distcenter >> num2) {
        distCoeff_center.push_back(num2);
    }

    matcenter.close();
    distcenter.close();
    Mat intrinsic_matrix_center = (Mat_<double>(3,3) << a[0], a[1], a[2], a[3],a[4], a[5], a[6], a[7], a[8]);
    Mat R=Mat::eye(3, 3, CV_8U);
	initUndistortRectifyMap(intrinsic_matrix_center, distCoeff_center, R, intrinsic_matrix_center, Size (1280,720), CV_32FC1, map1_center, map2_center);
    a.clear();
    distCoeff_center.clear();
    intrinsic_matrix_center.release();
    
    //string s="1/"+i+".png";

    // Sending a number as a stream into output
    // string
    // the str() coverts number into string
    string geek1 = "1.png";
    string geek2 = "2.png";

    Mat image = imread(geek1);
    Mat image2 = imread(geek1);
        
    remap(image, image2, map1_center, map2_center, CV_INTER_LINEAR);
    imwrite(geek2,image2);

}