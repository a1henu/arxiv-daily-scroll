---
layout: default
title: Probabilistic Multi-Agent Aircraft Landing Time Prediction
---

# Probabilistic Multi-Agent Aircraft Landing Time Prediction
**arXiv**：[2512.08281v1](https://arxiv.org/abs/2512.08281) · [PDF](https://arxiv.org/pdf/2512.08281.pdf)  
**作者**：Kyungmin Kim, Seokbin Yoon, Keumjin Lee  

**一句话要点**：提出概率多智能体飞机着陆时间预测框架，以提升空管资源分配中的准确性和不确定性量化。

**关键词**：飞机着陆时间预测, 概率预测, 多智能体交互, 空管不确定性, 可解释性模型

## 3 点简述
- 核心问题：飞机轨迹和交通流的不确定性挑战着陆时间预测的准确性和可信度。
- 方法要点：采用概率多智能体框架，预测多架飞机着陆时间的分布，并考虑空域交互。
- 实验或效果：在仁川国际机场数据集上验证，模型优于基线，提供不确定性量化和可解释性。

## 摘要（原文）

> Accurate and reliable aircraft landing time prediction is essential for effective resource allocation in air traffic management. However, the inherent uncertainty of aircraft trajectories and traffic flows poses significant challenges to both prediction accuracy and trustworthiness. Therefore, prediction models should not only provide point estimates of aircraft landing times but also the uncertainties associated with these predictions. Furthermore, aircraft trajectories are frequently influenced by the presence of nearby aircraft through air traffic control interventions such as radar vectoring. Consequently, landing time prediction models must account for multi-agent interactions in the airspace. In this work, we propose a probabilistic multi-agent aircraft landing time prediction framework that provides the landing times of multiple aircraft as distributions. We evaluate the proposed framework using an air traffic surveillance dataset collected from the terminal airspace of the Incheon International Airport in South Korea. The results demonstrate that the proposed model achieves higher prediction accuracy than the baselines and quantifies the associated uncertainties of its outcomes. In addition, the model uncovered underlying patterns in air traffic control through its attention scores, thereby enhancing explainability.

