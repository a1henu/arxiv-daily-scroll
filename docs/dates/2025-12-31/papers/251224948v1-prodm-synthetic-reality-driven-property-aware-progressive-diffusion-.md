---
layout: default
title: ProDM: Synthetic Reality-driven Property-aware Progressive Diffusion Model for Coronary Calcium Motion Correction in Non-gated Chest CT
---

# ProDM: Synthetic Reality-driven Property-aware Progressive Diffusion Model for Coronary Calcium Motion Correction in Non-gated Chest CT
**arXiv**：[2512.24948v1](https://arxiv.org/abs/2512.24948) · [PDF](https://arxiv.org/pdf/2512.24948.pdf)  
**作者**：Xinran Gong, Gorkem Durak, Halil Ertugrul Aktas, Vedat Cicek, Jinkui Hao, Ulas Bagci, Nilay S. Shah, Bo Zhou  

**一句话要点**：提出ProDM扩散模型以解决非门控胸部CT中冠状动脉钙化运动伪影校正问题

**关键词**：冠状动脉钙化评分, 运动伪影校正, 扩散模型, 合成数据生成, 属性感知学习, 渐进校正

## 3 点简述
- 核心问题：非门控胸部CT中冠状动脉钙化评分受心脏和呼吸运动伪影影响，限制临床应用。
- 方法要点：通过合成数据引擎、钙化属性感知学习和渐进校正策略，恢复无运动钙化病灶。
- 实验或效果：在真实数据集上显著提升钙化评分准确性、病灶保真度和风险分层性能。

## 摘要（原文）

> Coronary artery calcium (CAC) scoring from chest CT is a well-established tool to stratify and refine clinical cardiovascular disease risk estimation. CAC quantification relies on the accurate delineation of calcified lesions, but is oftentimes affected by artifacts introduced by cardiac and respiratory motion. ECG-gated cardiac CTs substantially reduce motion artifacts, but their use in population screening and routine imaging remains limited due to gating requirements and lack of insurance coverage. Although identification of incidental CAC from non-gated chest CT is increasingly considered for it offers an accessible and widely available alternative, this modality is limited by more severe motion artifacts. We present ProDM (Property-aware Progressive Correction Diffusion Model), a generative diffusion framework that restores motion-free calcified lesions from non-gated CTs. ProDM introduces three key components: (1) a CAC motion simulation data engine that synthesizes realistic non-gated acquisitions with diverse motion trajectories directly from cardiac-gated CTs, enabling supervised training without paired data; (2) a property-aware learning strategy incorporating calcium-specific priors through a differentiable calcium consistency loss to preserve lesion integrity; and (3) a progressive correction scheme that reduces artifacts gradually across diffusion steps to enhance stability and calcium fidelity. Experiments on real patient datasets show that ProDM significantly improves CAC scoring accuracy, spatial lesion fidelity, and risk stratification performance compared with several baselines. A reader study on real non-gated scans further confirms that ProDM suppresses motion artifacts and improves clinical usability. These findings highlight the potential of progressive, property-aware frameworks for reliable CAC quantification from routine chest CT imaging.

