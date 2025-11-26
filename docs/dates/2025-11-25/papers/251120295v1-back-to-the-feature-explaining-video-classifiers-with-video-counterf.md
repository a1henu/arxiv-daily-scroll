---
layout: default
title: Back to the Feature: Explaining Video Classifiers with Video Counterfactual Explanations
---

# Back to the Feature: Explaining Video Classifiers with Video Counterfactual Explanations
**arXiv**：[2511.20295v1](https://arxiv.org/abs/2511.20295) · [PDF](https://arxiv.org/pdf/2511.20295.pdf)  
**作者**：Chao Wang, Chengan Che, Xinyue Chen, Sophia Tsoka, Luis C. Garcia-Peraza-Herrera  

**一句话要点**：提出BTTF优化框架以生成视频分类器的反事实解释

**关键词**：反事实解释, 视频分类, 优化框架, 时间一致性, 物理合理性

## 3 点简述
- 现有反事实解释方法无法生成时间一致且物理合理的视频解释
- BTTF引入条件初始噪声和两阶段优化策略，仅依赖目标分类器指导
- 在多个视频数据集上验证，生成有效、相似且真实的视频解释

## 摘要（原文）

> Counterfactual explanations (CFEs) are minimal and semantically meaningful modifications of the input of a model that alter the model predictions. They highlight the decisive features the model relies on, providing contrastive interpretations for classifiers. State-of-the-art visual counterfactual explanation methods are designed to explain image classifiers. The generation of CFEs for video classifiers remains largely underexplored. For the counterfactual videos to be useful, they have to be physically plausible, temporally coherent, and exhibit smooth motion trajectories. Existing CFE image-based methods, designed to explain image classifiers, lack the capacity to generate temporally coherent, smooth and physically plausible video CFEs. To address this, we propose Back To The Feature (BTTF), an optimization framework that generates video CFEs. Our method introduces two novel features, 1) an optimization scheme to retrieve the initial latent noise conditioned by the first frame of the input video, 2) a two-stage optimization strategy to enable the search for counterfactual videos in the vicinity of the input video. Both optimization processes are guided solely by the target classifier, ensuring the explanation is faithful. To accelerate convergence, we also introduce a progressive optimization strategy that incrementally increases the number of denoising steps. Extensive experiments on video datasets such as Shape-Moving (motion classification), MEAD (emotion classification), and NTU RGB+D (action classification) show that our BTTF effectively generates valid, visually similar and realistic counterfactual videos that provide concrete insights into the classifier's decision-making mechanism.

