---
layout: default
title: RTFDNet: Fusion-Decoupling for Robust RGB-T Segmentation
---

# RTFDNet: Fusion-Decoupling for Robust RGB-T Segmentation
**arXiv**：[2603.09149v1](https://arxiv.org/abs/2603.09149) · [PDF](https://arxiv.org/pdf/2603.09149.pdf)  
**作者**：Kunyu Tan, Mingjian Liang  

**一句话要点**：提出RTFDNet融合-解耦网络以增强RGB-T语义分割在传感器信号缺失下的鲁棒性。

**关键词**：RGB-T语义分割, 模态融合, 解耦正则化, 鲁棒性增强, 多模态学习, 编码器-解码器网络

## 3 点简述
- 传统方法过度强调模态平衡，导致信号部分缺失时性能下降。
- RTFDNet通过协同特征融合和跨模态解耦正则化统一融合与解耦。
- 实验显示RTFDNet在不同模态条件下保持稳定性能，支持高效独立推理。

## 摘要（原文）

> RGB-Thermal (RGB-T) semantic segmentation is essential for robotic systems operating in low-light or dark environments. However, traditional approaches often overemphasize modality balance, resulting in limited robustness and severe performance degradation when sensor signals are partially missing. Recent advances such as cross-modal knowledge distillation and modality-adaptive fine-tuning attempt to enhance cross-modal interaction, but they typically decouple modality fusion and modality adaptation, requiring multi-stage training with frozen models or teacher-student frameworks. We present RTFDNet, a three-branch encoder-decoder that unifies fusion and decoupling for robust RGB-T segmentation. Synergistic Feature Fusion (SFF) performs channel-wise gated exchange and lightweight spatial attention to inject complementary cues. Cross-Modal Decouple Regularization (CMDR) isolates modality-specific components from the fused representation and supervises unimodal decoders via stop-gradient targets. Region Decouple Regularization (RDR) enforces class-selective prediction consistency in confident regions while blocking gradients to the fusion branch. This feedback loop strengthens unimodal paths without degrading the fused stream, enabling efficient standalone inference at test time. Extensive experiments demonstrate the effectiveness of RTFDNet, showing consistent performance across varying modality conditions. Our implementation will be released to facilitate further research. Our source code are publicly available at https://github.com/curapima/RTFDNet.

