---
layout: default
title: M3DDM+: An improved video outpainting by a modified masking strategy
---

# M3DDM+: An improved video outpainting by a modified masking strategy
**arXiv**：[2601.11048v1](https://arxiv.org/abs/2601.11048) · [PDF](https://arxiv.org/pdf/2601.11048.pdf)  
**作者**：Takuya Murakawa, Takumi Fukuzawa, Ning Ding, Toru Tamaki  

**一句话要点**：提出M3DDM+通过改进掩码策略以解决视频外绘在信息有限场景下的质量退化问题

**关键词**：视频外绘, 潜在扩散模型, 掩码策略, 时间一致性, 计算效率

## 3 点简述
- M3DDM在相机运动有限或外绘区域大时出现空间模糊和时间不一致问题
- M3DDM+在训练中应用统一掩码方向与宽度，并微调预训练模型
- 实验显示M3DDM+在信息有限场景下显著提升视觉保真度和时间一致性

## 摘要（原文）

> M3DDM provides a computationally efficient framework for video outpainting via latent diffusion modeling. However, it exhibits significant quality degradation -- manifested as spatial blur and temporal inconsistency -- under challenging scenarios characterized by limited camera motion or large outpainting regions, where inter-frame information is limited. We identify the cause as a training-inference mismatch in the masking strategy: M3DDM's training applies random mask directions and widths across frames, whereas inference requires consistent directional outpainting throughout the video. To address this, we propose M3DDM+, which applies uniform mask direction and width across all frames during training, followed by fine-tuning of the pretrained M3DDM model. Experiments demonstrate that M3DDM+ substantially improves visual fidelity and temporal coherence in information-limited scenarios while maintaining computational efficiency. The code is available at https://github.com/tamaki-lab/M3DDM-Plus.

