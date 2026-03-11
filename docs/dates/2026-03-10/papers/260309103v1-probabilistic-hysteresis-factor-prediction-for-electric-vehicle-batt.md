---
layout: default
title: Probabilistic Hysteresis Factor Prediction for Electric Vehicle Batteries with Graphite Anodes Containing Silicon
---

# Probabilistic Hysteresis Factor Prediction for Electric Vehicle Batteries with Graphite Anodes Containing Silicon
**arXiv**：[2603.09103v1](https://arxiv.org/abs/2603.09103) · [PDF](https://arxiv.org/pdf/2603.09103.pdf)  
**作者**：Runyao Yu, Viviana Kleine, Philipp Gromotka, Thomas Rudolf, Adrian Eisenmann, Gautham Ram Chandra Mouli, Peter Palensky, Jochen L. Cremer  

**一句话要点**：提出概率性滞后因子预测方法，以解决硅-石墨阳极电池的荷电状态估计挑战。

**关键词**：电池滞后预测, 硅-石墨阳极, 概率建模, 数据驱动方法, 荷电状态估计, 深度学习

## 3 点简述
- 核心问题：硅-石墨阳极电池存在显著电压滞后，导致荷电状态估计困难。
- 方法要点：采用数据驱动方法，结合数据标准化和统计与深度学习模型进行概率预测。
- 实验或效果：通过多种训练策略评估模型泛化能力，促进先进电池技术应用。

## 摘要（原文）

> Batteries with silicon-graphite-based anodes, which offer higher energy density and improved charging performance, introduce pronounced voltage hysteresis, making state-of-charge (SoC) estimation particularly challenging. Existing approaches to modeling hysteresis rely on exhaustive high-fidelity tests or focus on conventional graphite-based lithium-ion batteries, without considering uncertainty quantification or computational constraints. This work introduces a data-driven approach for probabilistic hysteresis factor prediction, with a particular emphasis on applications involving silicon-graphite anode-based batteries. A data harmonization framework is proposed to standardize heterogeneous driving cycles across varying operating conditions. Statistical learning and deep learning models are applied to assess performance in predicting the hysteresis factor with uncertainties while considering computational efficiency. Extensive experiments are conducted to evaluate the generalizability of the optimal model configuration in unseen vehicle models through retraining, zero-shot prediction, fine-tuning, and joint training. By addressing key challenges in SoC estimation, this research facilitates the adoption of advanced battery technologies. A summary page is available at: https://runyao-yu.github.io/Porsche_Hysteresis_Factor_Prediction/

