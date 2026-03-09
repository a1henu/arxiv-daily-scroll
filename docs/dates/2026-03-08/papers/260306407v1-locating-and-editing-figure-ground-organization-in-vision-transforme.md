---
layout: default
title: Locating and Editing Figure-Ground Organization in Vision Transformers
---

# Locating and Editing Figure-Ground Organization in Vision Transformers
**arXiv**：[2603.06407v1](https://arxiv.org/abs/2603.06407) · [PDF](https://arxiv.org/pdf/2603.06407.pdf)  
**作者**：Stefan Arnold, René Gröbner  

**一句话要点**：定位并编辑BEiT中基于凸性先验的图形-背景组织机制

**关键词**：图形-背景组织, 视觉Transformer, 感知模糊性, 注意力机制, BEiT模型, 凸性先验

## 3 点简述
- 研究视觉Transformer在局部几何证据与全局组织先验冲突下的图形-背景组织模糊性
- 通过合成飞镖形状的感知冲突实验，揭示BEiT偏好凸性完成，并定位到内部功能单元
- 识别注意力头L0H9作为早期种子，其缩放可连续调控感知决策边界

## 摘要（原文）

> Vision Transformers must resolve figure-ground organization by choosing between completions driven by local geometric evidence and those favored by global organizational priors, giving rise to a characteristic perceptual ambiguity. We aim to locate where the canonical Gestalt prior convexity is realized within the internal components of BEiT. Using a controlled perceptual conflict based on synthetic shapes of darts, we systematically mask regions that equally admit either a concave completion or a convex completion. We show that BEiT reliably favors convex completion under this competition. Projecting internal activations into the model's discrete visual codebook space via logit attribution reveals that this preference is governed by identifiable functional units within transformer substructures. Specifically, we find that figure-ground organization is ambiguous through early and intermediate layers and resolves abruptly in later layers. By decomposing the direct effect of attention heads, we identify head L0H9 acting as an early seed, introducing a weak bias toward convexity. Downscaling this single attention head shifts the distributional mass of the perceptual conflict across a continuous decision boundary, allowing concave evidence to guide completion.

