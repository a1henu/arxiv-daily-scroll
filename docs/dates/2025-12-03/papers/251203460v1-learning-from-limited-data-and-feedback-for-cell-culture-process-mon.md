---
layout: default
title: Learning From Limited Data and Feedback for Cell Culture Process Monitoring: A Comparative Study
---

# Learning From Limited Data and Feedback for Cell Culture Process Monitoring: A Comparative Study
**arXiv**：[2512.03460v1](https://arxiv.org/abs/2512.03460) · [PDF](https://arxiv.org/pdf/2512.03460.pdf)  
**作者**：Johnny Peng, Thanh Tung Khuat, Ellen Otte, Katarzyna Musial, Bogdan Gabrys  

**一句话要点**：比较机器学习方法以解决细胞培养过程监控中数据有限和反馈稀疏的挑战

**关键词**：细胞培养过程监控, 软传感器, 有限数据学习, 在线学习, 即时学习, 特征降维

## 3 点简述
- 核心问题：细胞培养过程监控面临历史数据有限、反馈稀疏、条件异质和高维输入等挑战，阻碍软传感器开发。
- 方法要点：评估特征降维、在线学习和即时学习等方法，在三个数据集上比较训练策略，包括同质和冷启动场景。
- 实验或效果：发现批处理学习在同质设置中有效，而即时学习和在线学习在冷启动中适应性更强；集成拉曼预测与滞后离线测量可提升准确性。

## 摘要（原文）

> In cell culture bioprocessing, real-time batch process monitoring (BPM) refers to the continuous tracking and analysis of key process variables such as viable cell density, nutrient levels, metabolite concentrations, and product titer throughout the duration of a batch run. This enables early detection of deviations and supports timely control actions to ensure optimal cell growth and product quality. BPM plays a critical role in ensuring the quality and regulatory compliance of biopharmaceutical manufacturing processes. However, the development of accurate soft sensors for BPM is hindered by key challenges, including limited historical data, infrequent feedback, heterogeneous process conditions, and high-dimensional sensory inputs. This study presents a comprehensive benchmarking analysis of machine learning (ML) methods designed to address these challenges, with a focus on learning from historical data with limited volume and relevance in the context of bioprocess monitoring. We evaluate multiple ML approaches including feature dimensionality reduction, online learning, and just-in-time learning across three datasets, one in silico dataset and two real-world experimental datasets. Our findings highlight the importance of training strategies in handling limited data and feedback, with batch learning proving effective in homogeneous settings, while just-in-time learning and online learning demonstrate superior adaptability in cold-start scenarios. Additionally, we identify key meta-features, such as feed media composition and process control strategies, that significantly impact model transferability. The results also suggest that integrating Raman-based predictions with lagged offline measurements enhances monitoring accuracy, offering a promising direction for future bioprocess soft sensor development.

