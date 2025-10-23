---
layout: default
title: Exploring Scale Shift in Crowd Localization under the Context of Domain Generalization
---

# Exploring Scale Shift in Crowd Localization under the Context of Domain Generalization
**arXiv**：[2510.19330v1](https://arxiv.org/abs/2510.19330) · [PDF](https://arxiv.org/pdf/2510.19330.pdf)  
**作者**：Juncheng Wang, Lei Shang, Ziqi Liu, Wang Lu, Xixu Hu, Zhe Hu, Jindong Wang, Shujun Wang  

**一句话要点**：提出Catto算法以缓解人群定位中尺度偏移对领域泛化的影响

**关键词**：人群定位, 领域泛化, 尺度偏移, 因果特征分解, 基准测试

## 3 点简述
- 核心问题：训练与测试数据中头部尺度分布差异导致人群定位性能下降
- 方法要点：通过因果特征分解与各向异性处理来减轻尺度偏移影响
- 实验或效果：建立ScaleBench基准，验证算法有效性并揭示现有方法局限

## 摘要（原文）

> Crowd localization plays a crucial role in visual scene understanding towards
> predicting each pedestrian location in a crowd, thus being applicable to
> various downstream tasks. However, existing approaches suffer from significant
> performance degradation due to discrepancies in head scale distributions (scale
> shift) between training and testing data, a challenge known as domain
> generalization (DG). This paper aims to comprehend the nature of scale shift
> within the context of domain generalization for crowd localization models. To
> this end, we address four critical questions: (i) How does scale shift
> influence crowd localization in a DG scenario? (ii) How can we quantify this
> influence? (iii) What causes this influence? (iv) How to mitigate the
> influence? Initially, we conduct a systematic examination of how crowd
> localization performance varies with different levels of scale shift. Then, we
> establish a benchmark, ScaleBench, and reproduce 20 advanced DG algorithms to
> quantify the influence. Through extensive experiments, we demonstrate the
> limitations of existing algorithms and underscore the importance and complexity
> of scale shift, a topic that remains insufficiently explored. To deepen our
> understanding, we provide a rigorous theoretical analysis on scale shift.
> Building on these insights, we further propose an effective algorithm called
> Causal Feature Decomposition and Anisotropic Processing (Catto) to mitigate the
> influence of scale shift in DG settings. Later, we also provide extensive
> analytical experiments, revealing four significant insights for future
> research. Our results emphasize the importance of this novel and applicable
> research direction, which we term Scale Shift Domain Generalization.

