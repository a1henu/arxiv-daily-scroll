---
layout: default
title: See Less, Drive Better: Generalizable End-to-End Autonomous Driving via Foundation Models Stochastic Patch Selection
---

# See Less, Drive Better: Generalizable End-to-End Autonomous Driving via Foundation Models Stochastic Patch Selection
**arXiv**：[2601.10707v1](https://arxiv.org/abs/2601.10707) · [PDF](https://arxiv.org/pdf/2601.10707.pdf)  
**作者**：Amir Mallak, Erfan Aasi, Shiva Sreeram, Tsun-Hsuan Wang, Daniela Rus, Alaa Maalouf  

**一句话要点**：提出随机补丁选择方法以提升端到端自动驾驶的泛化性与效率

**关键词**：端到端自动驾驶, 基础模型, 随机补丁选择, 泛化性, 分布外鲁棒性, 特征冗余

## 3 点简述
- 问题：基于基础模型提取的补丁特征冗余度高，导致策略过拟合虚假相关，损害分布外鲁棒性。
- 方法：提出随机补丁选择，每帧随机掩码部分补丁描述符，保持空间布局，提供不同随机但完整的场景视图。
- 效果：在分布外场景中平均提升6.2%，闭环模拟最高提升20.4%，速度提升2.4倍，无需调优即可迁移到真实车辆。

## 摘要（原文）

> Recent advances in end-to-end autonomous driving show that policies trained on patch-aligned features extracted from foundation models generalize better to Out-of-Distribution (OOD). We hypothesize that due to the self-attention mechanism, each patch feature implicitly embeds/contains information from all other patches, represented in a different way and intensity, making these descriptors highly redundant. We quantify redundancy in such (BLIP2) features via PCA and cross-patch similarity: $90$% of variance is captured by $17/64$ principal components, and strong inter-token correlations are pervasive. Training on such overlapping information leads the policy to overfit spurious correlations, hurting OOD robustness. We present Stochastic-Patch-Selection (SPS), a simple yet effective approach for learning policies that are more robust, generalizable, and efficient. For every frame, SPS randomly masks a fraction of patch descriptors, not feeding them to the policy model, while preserving the spatial layout of the remaining patches. Thus, the policy is provided with different stochastic but complete views of the (same) scene: every random subset of patches acts like a different, yet still sensible, coherent projection of the world. The policy thus bases its decisions on features that are invariant to which specific tokens survive. Extensive experiments confirm that across all OOD scenarios, our method outperforms the state of the art (SOTA), achieving a $6.2$% average improvement and up to $20.4$% in closed-loop simulations, while being $2.4\times$ faster. We conduct ablations over masking rates and patch-feature reorganization, training and evaluating 9 systems, with 8 of them surpassing prior SOTA. Finally, we show that the same learned policy transfers to a physical, real-world car without any tuning.

