---
layout: default
title: Modeling Cultural Bias in Facial Expression Recognition with Adaptive Agents
---

# Modeling Cultural Bias in Facial Expression Recognition with Adaptive Agents
**arXiv**：[2510.13557v1](https://arxiv.org/abs/2510.13557) · [PDF](https://arxiv.org/pdf/2510.13557.pdf)  
**作者**：David Freire-Obregón, José Salas-Cáceres, Javier Lorenzo-Navarro, Oliverio J. Santana, Daniel Hernández-Sosa, Modesto Castrillón-Santana  

**一句话要点**：提出基于自适应代理的流式基准，量化文化偏见与模糊对表情识别鲁棒性的影响

**关键词**：面部表情识别, 文化偏见建模, 自适应代理, 高斯模糊鲁棒性, 流式基准, 特征空间交互

## 3 点简述
- 核心问题：表情识别在文化差异和图像模糊下鲁棒性不足，现有评估假设数据同质和高质
- 方法要点：使用代理在CLIP特征空间移动交互，在线训练轻量残差适配器，环境提供高斯模糊输入
- 实验或效果：文化组性能曲线不对称，混合环境可缓解早期退化，不平衡设置放大弱点

## 摘要（原文）

> Facial expression recognition (FER) must remain robust under both cultural
> variation and perceptually degraded visual conditions, yet most existing
> evaluations assume homogeneous data and high-quality imagery. We introduce an
> agent-based, streaming benchmark that reveals how cross-cultural composition
> and progressive blurring interact to shape face recognition robustness. Each
> agent operates in a frozen CLIP feature space with a lightweight residual
> adapter trained online at sigma=0 and fixed during testing. Agents move and
> interact on a 5x5 lattice, while the environment provides inputs with
> sigma-scheduled Gaussian blur. We examine monocultural populations
> (Western-only, Asian-only) and mixed environments with balanced (5/5) and
> imbalanced (8/2, 2/8) compositions, as well as different spatial contact
> structures. Results show clear asymmetric degradation curves between cultural
> groups: JAFFE (Asian) populations maintain higher performance at low blur but
> exhibit sharper drops at intermediate stages, whereas KDEF (Western)
> populations degrade more uniformly. Mixed populations exhibit intermediate
> patterns, with balanced mixtures mitigating early degradation, but imbalanced
> settings amplify majority-group weaknesses under high blur. These findings
> quantify how cultural composition and interaction structure influence the
> robustness of FER as perceptual conditions deteriorate.

