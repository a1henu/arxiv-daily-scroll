---
layout: default
title: TraceRouter: Robust Safety for Large Foundation Models via Path-Level Intervention
---

# TraceRouter: Robust Safety for Large Foundation Models via Path-Level Intervention
**arXiv**：[2601.21900v1](https://arxiv.org/abs/2601.21900) · [PDF](https://arxiv.org/pdf/2601.21900.pdf)  
**作者**：Chuancheng Shi, Shangze Li, Wenjun Lu, Wenhua Wu, Cong Wang, Zifeng Cheng, Fei Shen, Tat-Seng Chua  

**一句话要点**：提出TraceRouter路径级干预框架，以增强大型基础模型对抗攻击的鲁棒性

**关键词**：大型基础模型, 对抗鲁棒性, 路径级干预, 因果传播电路, 稀疏自编码器, 注意力机制

## 3 点简述
- 核心问题：大型基础模型易受对抗攻击，现有防御基于局部假设，对分布式有害语义电路无效
- 方法要点：通过注意力差异定位敏感层，利用稀疏自编码器和特征影响分数追踪并切断恶意因果传播路径
- 实验或效果：实验显示TraceRouter在对抗鲁棒性和通用效用间取得优越平衡，显著优于现有基线

## 摘要（原文）

> Despite their capabilities, large foundation models (LFMs) remain susceptible to adversarial manipulation. Current defenses predominantly rely on the "locality hypothesis", suppressing isolated neurons or features. However, harmful semantics act as distributed, cross-layer circuits, rendering such localized interventions brittle and detrimental to utility. To bridge this gap, we propose \textbf{TraceRouter}, a path-level framework that traces and disconnects the causal propagation circuits of illicit semantics. TraceRouter operates in three stages: (1) it pinpoints a sensitive onset layer by analyzing attention divergence; (2) it leverages sparse autoencoders (SAEs) and differential activation analysis to disentangle and isolate malicious features; and (3) it maps these features to downstream causal pathways via feature influence scores (FIS) derived from zero-out interventions. By selectively suppressing these causal chains, TraceRouter physically severs the flow of harmful information while leaving orthogonal computation routes intact. Extensive experiments demonstrate that TraceRouter significantly outperforms state-of-the-art baselines, achieving a superior trade-off between adversarial robustness and general utility. Our code will be publicly released. WARNING: This paper contains unsafe model responses.

