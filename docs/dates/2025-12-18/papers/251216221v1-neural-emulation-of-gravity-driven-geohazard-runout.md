---
layout: default
title: Neural emulation of gravity-driven geohazard runout
---

# Neural emulation of gravity-driven geohazard runout
**arXiv**：[2512.16221v1](https://arxiv.org/abs/2512.16221) · [PDF](https://arxiv.org/pdf/2512.16221.pdf)  
**作者**：Lorenzo Nava, Ye Chen, Maximillian Van Wyk de Vries  

**一句话要点**：提出基于神经仿真的重力驱动地质灾害运移预测模型，实现快速准确预测

**关键词**：地质灾害运移预测, 神经仿真, 机器学习模型, 数值模拟, 计算效率, 早期预警系统

## 3 点简述
- 核心问题：地质灾害运移预测面临物理真实性与计算效率的权衡，现有方法难以兼顾。
- 方法要点：训练机器学习模型，利用超过10万次数值模拟数据，在真实地形上预测流动范围和沉积厚度。
- 实验或效果：模型预测准确度高，计算速度比数值求解器快100至10,000倍，能泛化到不同流动类型和地形。

## 摘要（原文）

> Predicting geohazard runout is critical for protecting lives, infrastructure and ecosystems. Rapid mass flows, including landslides and avalanches, cause several thousand deaths across a wide range of environments, often travelling many kilometres from their source. The wide range of source conditions and material properties governing these flows makes their runout difficult to anticipate, particularly for downstream communities that may be suddenly exposed to severe impacts. Accurately predicting runout at scale requires models that are both physically realistic and computationally efficient, yet existing approaches face a fundamental speed-realism trade-off. Here we train a machine learning model to predict geohazard runout across representative real world terrains. The model predicts both flow extent and deposit thickness with high accuracy and 100 to 10,000 times faster computation than numerical solvers. It is trained on over 100,000 numerical simulations across over 10,000 real world digital elevation model chips and reproduces key physical behaviours, including avulsion and deposition patterns, while generalizing across different flow types, sizes and landscapes. Our results demonstrate that neural emulation enables rapid, spatially resolved runout prediction across diverse real world terrains, opening new opportunities for disaster risk reduction and impact-based forecasting. These results highlight neural emulation as a promising pathway for extending physically realistic geohazard modelling to spatial and temporal scales relevant for large scale early warning systems.

