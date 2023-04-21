#!/bin/bash

#nohup python clustering.py --dataset Diff_Size_1 --method Kmeans --clusters 5 --pca 100 >./result/Kmeans_1_1.log &
#nohup python clustering.py --dataset Diff_Size_2 --method Kmeans --clusters 5 --pca 100 >./result/Kmeans_1_2.log &
#nohup python clustering.py --dataset Diff_Size_3 --method Kmeans --clusters 5 --pca 100 >./result/Kmeans_1_3.log &
#
#nohup python clustering.py --dataset Diff_Size_1 --method GMM --clusters 5 --pca 100 >./result/GMM_1_1.log &
#nohup python clustering.py --dataset Diff_Size_2 --method GMM --clusters 5 --pca 100 >./result/GMM_1_2.log &
#nohup python clustering.py --dataset Diff_Size_3 --method GMM --clusters 5 --pca 100 >./result/GMM_1_3.log &
#
#nohup python clustering.py --dataset Diff_Size_1 --method SOM --clusters 5 --pca 100 >./result/SOM_1_1.log &
#nohup python clustering.py --dataset Diff_Size_2 --method SOM --clusters 5 --pca 100 >./result/SOM_1_2.log &
#nohup python clustering.py --dataset Diff_Size_3 --method SOM --clusters 5 --pca 100 >./result/SOM_1_3.log &
#
#nohup python clustering.py --dataset Diff_Size_1 --method CFSFDP --clusters 5 --pca 100 >./result/CFSFDP_1_1.log &
#nohup python clustering.py --dataset Diff_Size_2 --method CFSFDP --clusters 5 --pca 100 >./result/CFSFDP_1_2.log &
#nohup python clustering.py --dataset Diff_Size_3 --method CFSFDP --clusters 5 --pca 100 >./result/CFSFDP_1_3.log &
#
#nohup python clustering.py --dataset Diff_Size_1 --method HierarchicalClustering --clusters 5 --pca 100 >./result/HierarchicalClustering_1_1.log &
#nohup python clustering.py --dataset Diff_Size_2 --method HierarchicalClustering --clusters 5 --pca 100 >./result/HierarchicalClustering_1_2.log &
#nohup python clustering.py --dataset Diff_Size_3 --method HierarchicalClustering --clusters 5 --pca 100 >./result/HierarchicalClustering_1_3.log &
#
#nohup python clustering.py --dataset Diff_Size_1 --method DBSCAN --clusters 5 --pca 100 >./result/DBSCAN_1_1.log &
#nohup python clustering.py --dataset Diff_Size_2 --method DBSCAN --clusters 5 --pca 100 >./result/DBSCAN_1_2.log &
#nohup python clustering.py --dataset Diff_Size_3 --method DBSCAN --clusters 5 --pca 100 >./result/DBSCAN_1_3.log &
#
#nohup python clustering.py --dataset Diff_Size_1 --method KmeansDP --clusters 5 --pca 100 >./result/KmeansDP_1_1.log &
#nohup python clustering.py --dataset Diff_Size_2 --method KmeansDP --clusters 5 --pca 100 >./result/KmeansDP_1_2.log &
#nohup python clustering.py --dataset Diff_Size_3 --method KmeansDP --clusters 5 --pca 100 >./result/KmeansDP_1_3.log &
#
#nohup python clustering.py --dataset Diff_Size_1 --method Kmedoids --clusters 5 --pca 100 >./result/Kmedoids_1_1.log &
#nohup python clustering.py --dataset Diff_Size_2 --method Kmedoids --clusters 5 --pca 100 >./result/Kmedoids_1_2.log &
#nohup python clustering.py --dataset Diff_Size_3 --method Kmedoids --clusters 5 --pca 100 >./result/Kmedoids_1_3.log &
###################################################
#nohup python clustering.py --dataset Diff_SNR_h --method Kmeans --clusters 5 --pca 0 >./result/Kmeans_Diff-SNR_1.log
#nohup python clustering.py --dataset Diff_SNR_m --method Kmeans --clusters 5 --pca 0 >./result/Kmeans_Diff-SNR_2.log
#nohup python clustering.py --dataset Diff_SNR_l --method Kmeans --clusters 5 --pca 0 >./result/Kmeans_Diff-SNR_3.log
#
#nohup python clustering.py --dataset Diff_SNR_h --method GMM --clusters 5 --pca 0 >./result/GMM_Diff-SNR_1.log
#nohup python clustering.py --dataset Diff_SNR_m --method GMM --clusters 5 --pca 0 >./result/GMM_Diff-SNR_2.log
#nohup python clustering.py --dataset Diff_SNR_l --method GMM --clusters 5 --pca 0 >./result/GMM_Diff-SNR_3.log
#
#nohup python clustering.py --dataset Diff_SNR_h --method SOM --clusters 5 --pca 0 >./result/SOM_Diff-SNR_1.log
#nohup python clustering.py --dataset Diff_SNR_m --method SOM --clusters 5 --pca 0 >./result/SOM_Diff-SNR_2.log
#nohup python clustering.py --dataset Diff_SNR_l --method SOM --clusters 5 --pca 0 >./result/SOM_Diff-SNR_3.log
#
#nohup python clustering.py --dataset Diff_SNR_h --method CFSFDP --clusters 5 --pca 0 >./result/CFSFDP_Diff-SNR_1.log
#nohup python clustering.py --dataset Diff_SNR_m --method CFSFDP --clusters 5 --pca 0 >./result/CFSFDP_Diff-SNR_2.log
#nohup python clustering.py --dataset Diff_SNR_l --method CFSFDP --clusters 5 --pca 0 >./result/CFSFDP_Diff-SNR_3.log
#
#nohup python clustering.py --dataset Diff_SNR_h --method HierarchicalClustering --clusters 5 --pca 0 >./result/HierarchicalClustering_Diff-SNR_1.log
#nohup python clustering.py --dataset Diff_SNR_m --method HierarchicalClustering --clusters 5 --pca 0 >./result/HierarchicalClustering_Diff-SNR_2.log
#nohup python clustering.py --dataset Diff_SNR_l --method HierarchicalClustering --clusters 5 --pca 0 >./result/HierarchicalClustering_Diff-SNR_3.log
#
#nohup python clustering.py --dataset Diff_SNR_h --method DBSCAN --clusters 5 --pca 0 >./result/DBSCAN_Diff-SNR_1.log
#nohup python clustering.py --dataset Diff_SNR_m --method DBSCAN --clusters 5 --pca 0 >./result/DBSCAN_Diff-SNR_2.log
#nohup python clustering.py --dataset Diff_SNR_l --method DBSCAN --clusters 5 --pca 0 >./result/DBSCAN_Diff-SNR_3.log
#
#nohup python clustering.py --dataset Diff_SNR_h --method KmeansDP --clusters 5 --pca 0 >./result/KmeansDP_Diff-SNR_1.log
#nohup python clustering.py --dataset Diff_SNR_m --method KmeansDP --clusters 5 --pca 0 >./result/KmeansDP_Diff-SNR_2.log
#nohup python clustering.py --dataset Diff_SNR_l --method KmeansDP --clusters 5 --pca 0 >./result/KmeansDP_Diff-SNR_3.log
#
#nohup python clustering.py --dataset Diff_SNR_h --method Kmedoids --clusters 5 --pca 0 >./result/Kmedoids_Diff-SNR_1.log
#nohup python clustering.py --dataset Diff_SNR_m --method Kmedoids --clusters 5 --pca 0 >./result/Kmedoids_Diff-SNR_2.log
#nohup python clustering.py --dataset Diff_SNR_l --method Kmedoids --clusters 5 --pca 0 >./result/Kmedoids_Diff-SNR_3.log

#####################################################
#nohup python clustering.py --dataset SGQ --method Kmeans --clusters 4 --pca 0 >./result/Kmeans_sgq_1.log
#nohup python clustering.py --dataset SGQ --method Kmeans --clusters 4 --pca 100 >./result/Kmeans_sgq_2.log
#
#nohup python clustering.py --dataset SGQ --method GMM --clusters 4 --pca 0 >./result/GMM_sgq_1.log
#nohup python clustering.py --dataset SGQ --method GMM --clusters 4 --pca 100 >./result/GMM_sgq_2.log
#
#nohup python clustering.py --dataset SGQ --method SOM --clusters 4 --pca 0 >./result/SOM_sgq_1.log
#nohup python clustering.py --dataset SGQ --method SOM --clusters 4 --pca 100 >./result/SOM_sgq_2.log
#
#nohup python clustering.py --dataset SGQ --method CFSFDP --clusters 4 --pca 0 >./result/CFSFDP_sgq_1.log
#nohup python clustering.py --dataset SGQ --method CFSFDP --clusters 4 --pca 100 >./result/CFSFDP_sgq_2.log
#
#nohup python clustering.py --dataset SGQ --method HierarchicalClustering --clusters 4 --pca 0 >./result/HierarchicalClustering_sgq_1.log
#nohup python clustering.py --dataset SGQ --method HierarchicalClustering --clusters 4 --pca 100 >./result/HierarchicalClustering_sgq_2.log
#
#nohup python clustering.py --dataset SGQ --method DBSCAN --clusters 4 --pca 0 >./result/DBSCAN_sgq_1.log
#nohup python clustering.py --dataset SGQ --method DBSCAN --clusters 4 --pca 100 >./result/DBSCAN_sgq_2.log
#
#nohup python clustering.py --dataset SGQ --method KmeansDP --clusters 4 --pca 0 >./result/KmeansDP_sgq_1.log
#nohup python clustering.py --dataset SGQ --method KmeansDP --clusters 4 --pca 100 >./result/KmeansDP_sgq_2.log
#
#nohup python clustering.py --dataset SGQ --method Kmedoids --clusters 4 --pca 0 >./result/Kmedoids_sgq_1.log
#nohup python clustering.py --dataset SGQ --method Kmedoids --clusters 4 --pca 100 >./result/Kmedoids_sgq_2.log


#############################
nohup python clustering.py --dataset Diff_SNR_h --method Kmeans --clusters 5 --pca 100 >./result/Kmeans_Diff-SNR-pca_1.log
nohup python clustering.py --dataset Diff_SNR_m --method Kmeans --clusters 5 --pca 100 >./result/Kmeans_Diff-SNR-pca_2.log
nohup python clustering.py --dataset Diff_SNR_l --method Kmeans --clusters 5 --pca 100 >./result/Kmeans_Diff-SNR-pca_3.log

nohup python clustering.py --dataset Diff_SNR_h --method GMM --clusters 5 --pca 100 >./result/GMM_Diff-SNR-pca_1.log
nohup python clustering.py --dataset Diff_SNR_m --method GMM --clusters 5 --pca 100 >./result/GMM_Diff-SNR-pca_2.log
nohup python clustering.py --dataset Diff_SNR_l --method GMM --clusters 5 --pca 100 >./result/GMM_Diff-SNR-pca_3.log

nohup python clustering.py --dataset Diff_SNR_h --method SOM --clusters 5 --pca 100 >./result/SOM_Diff-SNR-pca_1.log
nohup python clustering.py --dataset Diff_SNR_m --method SOM --clusters 5 --pca 100 >./result/SOM_Diff-SNR-pca_2.log
nohup python clustering.py --dataset Diff_SNR_l --method SOM --clusters 5 --pca 100 >./result/SOM_Diff-SNR-pca_3.log

nohup python clustering.py --dataset Diff_SNR_h --method CFSFDP --clusters 5 --pca 100 >./result/CFSFDP_Diff-SNR-pca_1.log
nohup python clustering.py --dataset Diff_SNR_m --method CFSFDP --clusters 5 --pca 100 >./result/CFSFDP_Diff-SNR-pca_2.log
nohup python clustering.py --dataset Diff_SNR_l --method CFSFDP --clusters 5 --pca 100 >./result/CFSFDP_Diff-SNR-pca_3.log

nohup python clustering.py --dataset Diff_SNR_h --method HierarchicalClustering --clusters 5 --pca 100 >./result/HierarchicalClustering_Diff-SNR-pca_1.log
nohup python clustering.py --dataset Diff_SNR_m --method HierarchicalClustering --clusters 5 --pca 100 >./result/HierarchicalClustering_Diff-SNR-pca_2.log
nohup python clustering.py --dataset Diff_SNR_l --method HierarchicalClustering --clusters 5 --pca 100 >./result/HierarchicalClustering_Diff-SNR-pca_3.log

nohup python clustering.py --dataset Diff_SNR_h --method DBSCAN --clusters 5 --pca 100 >./result/DBSCAN_Diff-SNR-pca_1.log
nohup python clustering.py --dataset Diff_SNR_m --method DBSCAN --clusters 5 --pca 100 >./result/DBSCAN_Diff-SNR-pca_2.log
nohup python clustering.py --dataset Diff_SNR_l --method DBSCAN --clusters 5 --pca 100 >./result/DBSCAN_Diff-SNR-pca_3.log

nohup python clustering.py --dataset Diff_SNR_h --method KmeansDP --clusters 5 --pca 100 >./result/KmeansDP_Diff-SNR-pca_1.log
nohup python clustering.py --dataset Diff_SNR_m --method KmeansDP --clusters 5 --pca 100 >./result/KmeansDP_Diff-SNR-pca_2.log
nohup python clustering.py --dataset Diff_SNR_l --method KmeansDP --clusters 5 --pca 100 >./result/KmeansDP_Diff-SNR-pca_3.log

nohup python clustering.py --dataset Diff_SNR_h --method Kmedoids --clusters 5 --pca 100 >./result/Kmedoids_Diff-SNR-pca_1.log
nohup python clustering.py --dataset Diff_SNR_m --method Kmedoids --clusters 5 --pca 100 >./result/Kmedoids_Diff-SNR-pca_2.log
nohup python clustering.py --dataset Diff_SNR_l --method Kmedoids --clusters 5 --pca 100 >./result/Kmedoids_Diff-SNR-pca_3.log
