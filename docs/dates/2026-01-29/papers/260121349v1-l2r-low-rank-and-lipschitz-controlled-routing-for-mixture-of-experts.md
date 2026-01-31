---
layout: default
title: L2R: Low-Rank and Lipschitz-Controlled Routing for Mixture-of-Experts
---

# L2R: Low-Rank and Lipschitz-Controlled Routing for Mixture-of-Experts
**arXiv**：[2601.21349v1](https://arxiv.org/abs/2601.21349) · [PDF](https://arxiv.org/pdf/2601.21349.pdf)  
**作者**：Minghao Yang, Ren Togo, Guang Li, Takahiro Ogawa, Miki Haseyama  

**一句话要点**：提出L2R路由框架以解决MoE模型中线性路由的判别性与稳定性问题

**关键词**：混合专家模型, 路由机制, 低秩表示, Lipschitz控制, 多锚点路由, 模型稳定性

## 3 点简述
- 核心问题：MoE模型中线性路由在原始高维空间存在表示不匹配、角度集中和尺度敏感评分，影响路由判别性和专家稳定性。
- 方法要点：L2R在共享低秩潜在路由空间进行专家分配，引入饱和内积评分控制路由函数的Lipschitz行为，并采用参数高效的多锚点路由机制。
- 实验或效果：在大规模语言MoE模型和ImageNet视觉MoE设置中，L2R一致提升了路由稳定性、专家专业化和整体模型性能。

## 摘要（原文）

> Mixture-of-Experts (MoE) models scale neural networks by conditionally activating a small subset of experts, where the router plays a central role in determining expert specialization and overall model performance. However, many modern MoE systems still adopt linear routers in raw high-dimensional representation spaces, where representation mismatch, angular concentration, and scale-sensitive scoring can jointly undermine routing discriminability and stable expert specialization. In this work, we propose Low-rank \& Lipschitz-controlled Routing (L2R), a unified routing framework that reshapes both the routing space and scoring geometry. L2R performs expert assignment in a shared low-rank latent routing space and introduces Saturated Inner-Product Scoring (SIPS) to explicitly control the Lipschitz behavior of routing functions, yielding smoother and more stable routing geometry. In addition, L2R incorporates a parameter-efficient multi-anchor routing mechanism to enhance expert expressiveness. Extensive experiments on a large-scale language MoE model and a vision MoE setting on ImageNet demonstrate that L2R consistently improves routing stability, expert specialization, and overall model performance.

