---
layout: default
title: Parameter-Efficient Domain Adaptation of Physics-Informed Self-Attention based GNNs for AC Power Flow Prediction
---

# Parameter-Efficient Domain Adaptation of Physics-Informed Self-Attention based GNNs for AC Power Flow Prediction
**arXiv**：[2602.18227v1](https://arxiv.org/abs/2602.18227) · [PDF](https://arxiv.org/pdf/2602.18227.pdf)  
**作者**：Redwanul Karim, Changhun Kim, Timon Conrad, Nora Gourmelon, Julian Oelhaf, David Riebesel, Tomás Arias-Vergara, Andreas Maier, Johann Jäger, Siming Bayer  

**一句话要点**：提出LoRA+PHead方法，用于物理信息自注意力GNN的参数高效域适应，以解决交流潮流预测中的电压域偏移问题。

**关键词**：参数高效域适应, 物理信息图神经网络, 交流潮流预测, 低秩适应, 电压域偏移, 基尔霍夫一致性

## 3 点简述
- 核心问题：交流潮流预测模型在从中压电网迁移到高压电网时面临域偏移，传统全微调方法成本高且稳定性-可塑性权衡控制有限。
- 方法要点：采用LoRA对注意力投影进行低秩更新，并选择性解冻预测头，结合物理损失确保基尔霍夫一致性，实现参数高效域适应。
- 实验或效果：在多种电网拓扑中，LoRA+PHead以85.46%参数减少恢复近全微调精度，目标域RMSE差距为2.6×10^-4，物理残差可比。

## 摘要（原文）

> Accurate AC-PF prediction under domain shift is critical when models trained on medium-voltage (MV) grids are deployed on high-voltage (HV) networks. Existing physics-informed graph neural solvers typically rely on full fine-tuning for cross-regime transfer, incurring high retraining cost and offering limited control over the stability-plasticity trade-off between target-domain adaptation and source-domain retention. We study parameter-efficient domain adaptation for physics-informed self-attention based GNN, encouraging Kirchhoff-consistent behavior via a physics-based loss while restricting adaptation to low-rank updates. Specifically, we apply LoRA to attention projections with selective unfreezing of the prediction head to regulate adaptation capacity. This design yields a controllable efficiency-accuracy trade-off for physics-constrained inverse estimation under voltage-regime shift. Across multiple grid topologies, the proposed LoRA+PHead adaptation recovers near-full fine-tuning accuracy with a target-domain RMSE gap of $2.6\times10^{-4}$ while reducing the number of trainable parameters by 85.46%. The physics-based residual remains comparable to full fine-tuning; however, relative to Full FT, LoRA+PHead reduces MV source retention by 4.7 percentage points (17.9% vs. 22.6%) under domain shift, while still enabling parameter-efficient and physically consistent AC-PF estimation.

