---
layout: default
title: A Deep Surrogate Model for Robust and Generalizable Long-Term Blast Wave Prediction
---

# A Deep Surrogate Model for Robust and Generalizable Long-Term Blast Wave Prediction
**arXiv**：[2602.18168v1](https://arxiv.org/abs/2602.18168) · [PDF](https://arxiv.org/pdf/2602.18168.pdf)  
**作者**：Danning Jing, Xinhai Chen, Xifeng Pu, Jie Hu, Chao Huang, Xuguang Chen, Qinglin Wang, Jie Liu  

**一句话要点**：提出RGD-Blast模型以解决爆炸波长期预测中的鲁棒性和泛化性问题

**关键词**：爆炸波预测, 深度学习代理模型, 多尺度建模, 泛化能力, 长期预测, 鲁棒性

## 3 点简述
- 核心问题：爆炸波建模因非线性、计算成本高和现有机器学习模型在复杂场景下精度下降而具挑战性
- 方法要点：结合多尺度模块和动态-静态特征耦合机制，减少误差累积并增强泛化能力
- 实验或效果：在未见布局上实现高精度预测，速度比传统方法快两个数量级

## 摘要（原文）

> Accurately modeling the spatio-temporal dynamics of blast wave propagation remains a longstanding challenge due to its highly nonlinear behavior, sharp gradients, and burdensome computational cost. While machine learning-based surrogate models offer fast inference as a promising alternative, they suffer from degraded accuracy, particularly evaluated on complex urban layouts or out-of-distribution scenarios. Moreover, autoregressive prediction strategies in such models are prone to error accumulation over long forecasting horizons, limiting their robustness for extended-time simulations. To address these limitations, we propose RGD-Blast, a robust and generalizable deep surrogate model for high-fidelity, long-term blast wave forecasting. RGD-Blast incorporates a multi-scale module to capture both global flow patterns and local boundary interactions, effectively mitigating error accumulation during autoregressive prediction. We introduce a dynamic-static feature coupling mechanism that fuses time-varying pressure fields with static source and layout features, thereby enhancing out-of-distribution generalization. Experiments demonstrate that RGD-Blast achieves a two-order-of-magnitude speedup over traditional numerical methods while maintaining comparable accuracy. In generalization tests on unseen building layouts, the model achieves an average RMSE below 0.01 and an R2 exceeding 0.89 over 280 consecutive time steps. Additional evaluations under varying blast source locations and explosive charge weights further validate its generalization, substantially advancing the state of the art in long-term blast wave modeling.

