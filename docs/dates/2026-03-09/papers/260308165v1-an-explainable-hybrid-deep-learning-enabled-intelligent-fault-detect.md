---
layout: default
title: An explainable hybrid deep learning-enabled intelligent fault detection and diagnosis approach for automotive software systems validation
---

# An explainable hybrid deep learning-enabled intelligent fault detection and diagnosis approach for automotive software systems validation
**arXiv**：[2603.08165v1](https://arxiv.org/abs/2603.08165) · [PDF](https://arxiv.org/pdf/2603.08165.pdf)  
**作者**：Mohammad Abboush, Ehab Ghannoum, Andreas Rausch  

**一句话要点**：提出可解释混合深度学习模型以解决汽车软件系统验证中故障检测与诊断的黑盒问题

**关键词**：可解释人工智能, 故障检测与诊断, 汽车软件系统, 混合深度学习, 根因分析, 实时验证

## 3 点简述
- 核心问题：黑盒故障检测与诊断模型缺乏可解释性，阻碍预测原因理解和模型自适应，增加计算成本并限制实时安全应用信心。
- 方法要点：开发基于1dCNN-GRU的混合智能模型分析实时验证记录，并应用IGs、DeepLIFT、Gradient SHAP和DeepLIFT SHAP等可解释AI技术实现模型自适应和根因分析。
- 实验或效果：应用于硬件在环系统虚拟测试驾驶收集的实时数据集，未知具体性能指标。

## 摘要（原文）

> Advancements in data-driven machine learning have emerged as a pivotal element in supporting automotive software systems (ASSs) engineering across various levels of the V-development process. Duringsystemverificationandvalidation,theintegrationofanintelligent fault detection anddiagnosis (FDD) model with test recordings analysis process serves as a powerful tool for efficiency ensuring functional safety. However, the lack of interpretability of the black-box FDD models developed not only hinders understanding of the cause underlying the prediction, but also prevents the model from being adapted based on the prediction result. This, in turn, increases the computational cost required for developingacomplexFDDmodelandlimitsconfidenceinreal-timesafety-criticalapplications.To address this challenge, a novel explainable method for fault detection, identification, and localization is proposed in this article with the aim of providing a clear understanding of the logic behind the prediction outcome. To this end, a hybrid 1dCNN-GRU-based intelligent model was developed to analyze the recordings from the real-time validation process of ASSs. The employment of explainable AI techniques, i.e., IGs, DeepLIFT, Gradient SHAP, and DeepLIFT SHAP, was instrumental in enabling model adaptation and facilitating the root cause analysis (RCA). The proposed approach is applied to the real time dataset collected during a virtual test drive performed by the user on hardware in the loop system.

