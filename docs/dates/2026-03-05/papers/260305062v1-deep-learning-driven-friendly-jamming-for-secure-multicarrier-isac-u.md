---
layout: default
title: Deep Learning-Driven Friendly Jamming for Secure Multicarrier ISAC Under Channel Uncertainty
---

# Deep Learning-Driven Friendly Jamming for Secure Multicarrier ISAC Under Channel Uncertainty
**arXiv**：[2603.05062v1](https://arxiv.org/abs/2603.05062) · [PDF](https://arxiv.org/pdf/2603.05062.pdf)  
**作者**：Bui Minh Tuan, Van-Dinh Nguyen, Diep N. Nguyen, Nguyen Linh Trung, Nguyen Van Huynh, Dinh Thai Hoang, Marwan Krunz, Eryk Dutkiewicz  

**一句话要点**：提出深度学习驱动的友好干扰框架，以增强信道不确定下多载波ISAC系统的物理层安全。

**关键词**：集成感知与通信, 物理层安全, 深度学习驱动, 友好干扰, 信道不确定性, 雷达感知

## 3 点简述
- 核心问题：在信道状态信息不完美和窃听者位置未知时，传统友好干扰方法依赖精确信息，难以保障多载波ISAC安全。
- 方法要点：利用雷达回波反馈引导定向干扰，结合基于f-散度的非参数费舍尔信息矩阵估计器，联合优化波束成形和干扰设计。
- 实验或效果：仿真显示，方案显著提升保密率、降低误块率，对信道不确定性和角度估计误差具有强鲁棒性。

## 摘要（原文）

> Integrated sensing and communication (ISAC) systems promise efficient spectrum utilization by jointly supporting radar sensing and wireless communication. This paper presents a deep learning-driven framework for enhancing physical-layer security in multicarrier ISAC systems under imperfect channel state information (CSI) and in the presence of unknown eavesdropper (Eve) locations. Unlike conventional ISAC-based friendly jamming (FJ) approaches that require Eve's CSI or precise angle-of-arrival (AoA) estimates, our method exploits radar echo feedback to guide directional jamming without explicit Eve's information. To enhance robustness to radar sensing uncertainty, we propose a radar-aware neural network that jointly optimizes beamforming and jamming by integrating a novel nonparametric Fisher Information Matrix (FIM) estimator based on f-divergence. The jamming design satisfies the Cramer-Rao lower bound (CRLB) constraints even in the presence of noisy AoA. For efficient implementation, we introduce a quantized tensor train-based encoder that reduces the model size by more than 100 times with negligible performance loss. We also integrate a non-overlapping secure scheme into the proposed framework, in which specific sub-bands can be dedicated solely to communication. Extensive simulations demonstrate that the proposed solution achieves significant improvements in secrecy rate, reduced block error rate (BLER), and strong robustness against CSI uncertainty and angular estimation errors, underscoring the effectiveness of the proposed deep learning-driven friendly jamming framework under practical ISAC impairments.

