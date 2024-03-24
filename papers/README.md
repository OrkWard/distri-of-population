## 论文
1. [A Study on the Spatical and temporal distribution of population in Yunnan Province Based on BigDate](./A_Study_on_the_Spatial_and_Temporal_Distribution_of_Population_in_Yunnan_Province_Based_on_BigDate.pdf)
  - 中文：基于大数据，云南省，人口的时空分布(2020)
  - 摘要：四五六次人口普查，使用 ArcGIS 和地统计方法
  - 评：方法不同于主流，可以看看
2. [High Resolution Population Distribution Maps for Southeast Asia in 2010 and 2015](./High_Resolution_Population_Distribution_Maps_for_Southeast_Asia_in_2010_and_2015.pdf)
  - 中文：2010、2015 年东南亚地区的高精度人口分布(2013)
  - 摘要：~100 米地理分辨率人口数据集，为每个国家提供。借助了从 Landset 中获取的居住地、土地覆盖和其他设施的辅助数据。并和其他两个全球数据集的结果进行了对比
  - 评：基于 AfriPop[1] 的方法，随机森林
3. [Landscan A Global Population Database For Estimating Populations At Risk](./Landscan_A_Global_Population_Database_For_Estimating_Populations_At_Risk.pdf)
  - 中文：LandScan，一个全球人口数据库，用于估计处于风险的人口数量（1998）
  - 评：具体方法未公开，可以看看，数据集拿来用
4. [WorldPop, open data for spatial demography](./WorldPop_Open_Data_For_Spatial_Demography.pdf)
  - 中文：WorldPop，用于地统计的开放数据集（2017）
  - 评：对该项目的概述，没有信息
5. [Disaggregating Census Data for Population Mapping Using Random Forests with Remotely-Sensed and Ancillary Data](./Disaggregating_Census_Data_for_Population_Mapping_Using_Random_Forests_with_Remotely-Sensed_and_Ancillary_Data.pdf)
  - 评：WorldPop 项目主要使用的方法（随机森林），需要看看
6. [High-resolution gridded population datasets for Latin America and the Caribbean using official statistics](./High-resolution_gridded_population_datasets_for_Latin_America_and_the_Caribbean_using_official_statistics.pdf)
  - 中文：拉丁美洲和加勒比的高分辨率人口分布，使用官方统计数据(2023)
  - 评: 使用了非常多的辅助数据, 随后使用随机森林进行建模. 研究仅对比了建筑面积, 建筑高度, 建筑体积几个因素对准确度的影响, 得出的结论是基于建筑分布的预测能有效提高人口分布的预测准确度.
7. popRF: Random Forest-informed Disaggregative Population Modelling and Mapping(./popRF_random_forest_informed_disaggregative_population_modelling_and_mapping.pdf)
  - 中文: popRF: 基于随机森林启发的人口反聚合及映射(2021)
  - 评: [6] 中随机森林算法的具体使用方式, 需要看看
8. Spatiotemporal Patterns of Population in mainland China 1990 to 2010(./Spatiotemporal_patterns_of_population_in_mainland_China_1990_to_2010.pdf)
  - 中文: 中国大陆 1990-2010 的人口时空分布模式(2015)
9. The spatial allocation of population: a review of large-scale gridded population data products and their fitness for use(./The_spatial_allocation_of_population_a_review_of_large_scale_gridded_population_data_products_and_their_fitness_for_use.pdf)
  - 评: [6] 中对最终结果有效性验证的方式, 需要看看



## 文摘
 - 影响人口分布的因素可以被分为两个类型: 连续变量和不连续变量. 连续变量包括: 地形; 坡度; 气候; 夜间光照密度等等. 不连续变量包括: 土地利用方式; 是否存在住宅和城市地区; 道路; 水体; 径流; 自然保护区等等.
