---
layout: default
title: AgriPINN: A Process-Informed Neural Network for Interpretable and Scalable Crop Biomass Prediction Under Water Stress
---

# AgriPINN: A Process-Informed Neural Network for Interpretable and Scalable Crop Biomass Prediction Under Water Stress
**arXiv**：[2601.16045v1](https://arxiv.org/abs/2601.16045) · [PDF](https://arxiv.org/pdf/2601.16045.pdf)  
**作者**：Yue Shi, Liangxiu Han, Xin Zhang, Tam Sobeih, Thomas Gaiser, Nguyen Huu Thuy, Dominik Behrend, Amit Kumar Srivastava, Krishnagopal Halder, Frank Ewert  

**一句话要点**：提出AgriPINN，一种过程信息神经网络，用于可解释和可扩展的水分胁迫下作物生物量预测。

**关键词**：作物生物量预测, 过程信息神经网络, 水分胁迫, 可解释深度学习, 时空预测, 农业建模

## 3 点简述
- 核心问题：数据驱动模型缺乏可解释性，过程模型难以大规模部署，需解决作物生物量预测的准确性和可扩展性。
- 方法要点：将生物物理作物生长微分方程作为可微分约束集成到深度学习主干中，实现生理一致性和模型可扩展性。
- 实验或效果：在德国397个区域的历史数据和田间实验中验证，AgriPINN在准确性和计算效率上优于先进深度学习和过程模型。

## 摘要（原文）

> Accurate prediction of crop above-ground biomass (AGB) under water stress is critical for monitoring crop productivity, guiding irrigation, and supporting climate-resilient agriculture. Data-driven models scale well but often lack interpretability and degrade under distribution shift, whereas process-based crop models (e.g. DSSAT, APSIM, LINTUL5) require extensive calibration and are difficult to deploy over large spatial domains. To address these limitations, we propose AgriPINN, a process-informed neural network that integrates a biophysical crop-growth differential equation as a differentiable constraint within a deep learning backbone. This design encourages physiologically consistent biomass dynamics under water-stress conditions while preserving model scalability for spatially distributed AGB prediction. AgriPINN recovers latent physiological variables, including leaf area index (LAI), absorbed photosynthetically active radiation (PAR), radiation use efficiency (RUE), and water-stress factors, without requiring direct supervision. We pretrain AgriPINN on 60 years of historical data across 397 regions in Germany and fine-tune it on three years of field experiments under controlled water treatments. Results show that AgriPINN consistently outperforms state-of-the-art deep-learning baselines (ConvLSTM-ViT, SLTF, CNN-Transformer) and the process-based LINTUL5 model in terms of accuracy (RMSE reductions up to $43\%$) and computational efficiency. By combining the scalability of deep learning with the biophysical rigor of process-based modeling, AgriPINN provides a robust and interpretable framework for spatio-temporal AGB prediction, offering practical value for planning of irrigation infrastructure, yield forecasting, and climate-adaptation planning.

