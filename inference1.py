#C:\Users\Saaket\Desktop\Feb9_GL>python train1.py
#Mean Squared Error (Gradient Boosting - Day Data): 10452.18257533478
#Checking whether there is an H2O instance running at http://localhost:54321. connected.
#--------------------------  -----------------------------
#H2O_cluster_uptime:         26 mins 39 secs
#H2O_cluster_timezone:       Asia/Kolkata
#H2O_data_parsing_timezone:  UTC
#H2O_cluster_version:        3.44.0.3
#H2O_cluster_version_age:    1 month and 21 days
#H2O_cluster_name:           H2O_from_python_Saaket_hrsp6z
#H2O_cluster_total_nodes:    1
#H2O_cluster_free_memory:    1009 Mb
#H2O_cluster_total_cores:    12
#H2O_cluster_allowed_cores:  12
#H2O_cluster_status:         locked, healthy
#H2O_connection_url:         http://localhost:54321
#H2O_connection_proxy:       {"http": null, "https": null}
#H2O_internal_security:      False
#Python_version:             3.9.13 final
#--------------------------  -----------------------------
#Parse progress: |████████████████████████████████████████████████████████████████ (done)| 100%
#AutoML progress: |█▎                                                             |   2%
#12:25:00.704: AutoML: XGBoost is not available; skipping it.

#AutoML progress: |███████████████████████████████████████████████████████████████ (done)| 100%
#model_id                                                    rmse       mse       mae     rmsle    mean_residual_deviance
#StackedEnsemble_AllModels_1_AutoML_4_20240211_122500     110.734   12262     70.8648  0.140367                   12262
#StackedEnsemble_BestOfFamily_1_AutoML_4_20240211_122500  118.635   14074.4   80.9493  0.143256                   14074.4
#GBM_grid_1_AutoML_4_20240211_122500_model_1              119.647   14315.5   79.6411  0.143921                   14315.5
#GBM_2_AutoML_4_20240211_122500                           126.145   15912.5   77.3024  0.138233                   15912.5
#GBM_4_AutoML_4_20240211_122500                           138.961   19310.2   89.6171  0.153049                   19310.2
#GBM_3_AutoML_4_20240211_122500                           146.166   21364.6   96.9567  0.149046                   21364.6
#GBM_5_AutoML_4_20240211_122500                           159.535   25451.5  104.718   0.147328                   25451.5
#XRT_1_AutoML_4_20240211_122500                           219.535   48195.5  142.718   0.185727                   48195.5
#DRF_1_AutoML_4_20240211_122500                           237.612   56459.6  158.019   0.188693                   56459.6
#GBM_1_AutoML_4_20240211_122500                           338.211  114387    248.689   0.22053                   114387
#[12 rows x 6 columns]

#Mean Squared Error (Gradient Boosting - Hourly Data): 28.525083395819518
#Parse progress: |████████████████████████████████████████████████████████████████ (done)| 100%
#AutoML progress: |█▎                                                             |   2%
#12:26:25.193: AutoML: XGBoost is not available; skipping it.

#AutoML progress: |███████████████████████████████████████████████████████████████ (done)| 100%
#model_id                                                    rmse       mse      mae        rmsle    mean_residual_deviance
#StackedEnsemble_AllModels_1_AutoML_5_20240211_122625     1.5893    2.52586  1.04718  nan                           2.52586
#StackedEnsemble_BestOfFamily_1_AutoML_5_20240211_122625  1.7111    2.92786  1.20524  nan                           2.92786
#DeepLearning_1_AutoML_5_20240211_122625                  3.03902   9.23567  2.08156  nan                           9.23567
#GBM_5_AutoML_5_20240211_122625                           3.07981   9.48522  1.82477    0.030444                    9.48522
#GBM_grid_1_AutoML_5_20240211_122625_model_1              3.09849   9.60065  1.89194    0.0286737                   9.60065
#GLM_1_AutoML_5_20240211_122625                           3.93716  15.5012   2.82732  nan                          15.5012
#GBM_2_AutoML_5_20240211_122625                           4.46203  19.9097   2.62176    0.0514703                  19.9097
#GBM_1_AutoML_5_20240211_122625                           5.0786   25.7922   2.20571    0.0283559                  25.7922
#GBM_3_AutoML_5_20240211_122625                           5.12794  26.2957   3.08829    0.0643694                  26.2957
#XRT_1_AutoML_5_20240211_122625                           6.59927  43.5503   3.61817    0.0850297                  43.5503
#[12 rows x 6 columns]

#Closing connection _sid_a404 at exit
#H2O session _sid_a404 closed.

#C:\Users\Saaket\Desktop\Feb9_GL>