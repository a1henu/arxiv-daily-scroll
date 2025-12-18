---
layout: default
title: Learning continuous SOC-dependent thermal decomposition kinetics for Li-ion cathodes using KA-CRNNs
---

# Learning continuous SOC-dependent thermal decomposition kinetics for Li-ion cathodes using KA-CRNNs
**arXiv**：[2512.15628v1](https://arxiv.org/abs/2512.15628) · [PDF](https://arxiv.org/pdf/2512.15628.pdf)  
**作者**：Benjamin C. Koenig, Sili Deng  

**一句话要点**：提出KA-CRNN框架以学习锂离子电池正极的连续SOC依赖热分解动力学

**关键词**：锂离子电池, 热失控预测, KA-CRNN, SOC依赖动力学, 可解释模型, DSC数据

## 3 点简述
- 现有模型无法捕捉SOC连续依赖的热失控行为，限制了预测准确性
- 应用KA-CRNN从DSC数据学习连续SOC依赖的动力学参数，嵌入反应路径
- 在NCA、NM和NMA正极上验证，模型重现DSC热释放特征并提供可解释机制

## 摘要（原文）

> Thermal runaway in lithium-ion batteries is strongly influenced by the state of charge (SOC). Existing predictive models typically infer scalar kinetic parameters at a full SOC or a few discrete SOC levels, preventing them from capturing the continuous SOC dependence that governs exothermic behavior during abuse conditions. To address this, we apply the Kolmogorov-Arnold Chemical Reaction Neural Network (KA-CRNN) framework to learn continuous and realistic SOC-dependent exothermic cathode-electrolyte interactions. We apply a physics-encoded KA-CRNN to learn SOC-dependent kinetic parameters for cathode-electrolyte decomposition directly from differential scanning calorimetry (DSC) data. A mechanistically informed reaction pathway is embedded into the network architecture, enabling the activation energies, pre-exponential factors, enthalpies, and related parameters to be represented as continuous and fully interpretable functions of the SOC. The framework is demonstrated for NCA, NM, and NMA cathodes, yielding models that reproduce DSC heat-release features across all SOCs and provide interpretable insight into SOC-dependent oxygen-release and phase-transformation mechanisms. This approach establishes a foundation for extending kinetic parameter dependencies to additional environmental and electrochemical variables, supporting more accurate and interpretable thermal-runaway prediction and monitoring.

