---
layout: default
title: Disentangling History and Propagation Dependencies in Cross-Subject Knee Contact Stress Prediction Using a Shared MeshGraphNet Backbone
---

# Disentangling History and Propagation Dependencies in Cross-Subject Knee Contact Stress Prediction Using a Shared MeshGraphNet Backbone
**arXiv**：[2601.08318v1](https://arxiv.org/abs/2601.08318) · [PDF](https://arxiv.org/pdf/2601.08318.pdf)  
**作者**：Zhengye Pan, Jianwei Zuo, Jiajia Luo  

**一句话要点**：提出共享MeshGraphNet骨干网络，通过历史编码解决跨受试者膝关节接触应力预测中的不确定性

**关键词**：膝关节接触应力预测, MeshGraphNet, 历史依赖编码, 跨受试者泛化, 深度学习代理模型, 有限元分析

## 3 点简述
- 核心问题：跨受试者膝关节接触应力预测中，不确定性主要源于时间历史依赖还是空间传播依赖
- 方法要点：使用共享MeshGraphNet骨干网络，设计四种模型变体以分离历史编码和空间传播调制
- 实验或效果：历史编码模型显著提升全局精度和峰值应力预测，空间传播调制无显著改进

## 摘要（原文）

> Background:Subject-specific finite element analysis accurately characterizes knee joint mechanics but is computationally expensive. Deep surrogate models provide a rapid alternative, yet their generalization across subjects under limited pose and load inputs remains unclear. It remains unclear whether the dominant source of prediction uncertainty arises from temporal history dependence or spatial propagation dependence. Methods:To disentangle these factors, we employed a shared MGN backbone with a fixed mesh topology. A dataset of running trials from nine subjects was constructed using an OpenSim-FEBio workflow. We developed four model variants to isolate specific dependencies: (1) a baseline MGN; (2) CT-MGN, incorporating a Control Transformer to encode short-horizon history; (3) MsgModMGN, applying state-conditioned modulation to message passing for adaptive propagation; (4) CT-MsgModMGN, combining both mechanisms. Models were evaluated using a rigorous grouped 3-fold cross-validation on unseen subjects.Results:The models incorporating history encoding significantly outperformed the baseline MGN and MsgModMGN in global accuracy and spatial consistency. Crucially, the CT module effectively mitigated the peak-shaving defect common in deep surrogates, significantly reducing peak stress prediction errors. In contrast, the spatial propagation modulation alone yielded no significant improvement over the baseline, and combining it with CT provided no additional benefit.Conclusion:Temporal history dependence, rather than spatial propagation modulation, is the primary driver of prediction uncertainty in cross-subject knee contact mechanics. Explicitly encoding short-horizon driver sequences enables the surrogate model to recover implicit phase information, thereby achieving superior fidelity in peak-stress capture and high-risk localization compared to purely state-based approaches.

