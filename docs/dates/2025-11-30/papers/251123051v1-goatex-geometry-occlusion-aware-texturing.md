---
layout: default
title: GOATex: Geometry & Occlusion-Aware Texturing
---

# GOATex: Geometry & Occlusion-Aware Texturing
**arXiv**：[2511.23051v1](https://arxiv.org/abs/2511.23051) · [PDF](https://arxiv.org/pdf/2511.23051.pdf)  
**作者**：Hyunjin Kim, Kunho Kim, Adam Lee, Wonkwang Lee  

**一句话要点**：提出GOATex方法，基于命中级别和扩散模型解决3D网格内外表面纹理生成中的遮挡问题。

**关键词**：3D网格纹理生成, 遮挡感知, 扩散模型, 命中级别, 可见性控制, UV空间混合

## 3 点简述
- 核心问题：现有方法缺乏处理遮挡内部表面的机制，导致纹理不完整和可见接缝。
- 方法要点：引入命中级别量化网格面相对深度，分阶段控制可见性并应用扩散模型逐层纹理化。
- 实验或效果：GOATex无需微调扩散模型，生成无缝高保真纹理，支持内外区域独立提示。

## 摘要（原文）

> We present GOATex, a diffusion-based method for 3D mesh texturing that generates high-quality textures for both exterior and interior surfaces. While existing methods perform well on visible regions, they inherently lack mechanisms to handle occluded interiors, resulting in incomplete textures and visible seams. To address this, we introduce an occlusion-aware texturing framework based on the concept of hit levels, which quantify the relative depth of mesh faces via multi-view ray casting. This allows us to partition mesh faces into ordered visibility layers, from outermost to innermost. We then apply a two-stage visibility control strategy that progressively reveals interior regions with structural coherence, followed by texturing each layer using a pretrained diffusion model. To seamlessly merge textures obtained across layers, we propose a soft UV-space blending technique that weighs each texture's contribution based on view-dependent visibility confidence. Empirical results demonstrate that GOATex consistently outperforms existing methods, producing seamless, high-fidelity textures across both visible and occluded surfaces. Unlike prior works, GOATex operates entirely without costly fine-tuning of a pretrained diffusion model and allows separate prompting for exterior and interior mesh regions, enabling fine-grained control over layered appearances. For more qualitative results, please visit our project page: https://goatex3d.github.io/.

