---
layout: default
title: Through the Lens: Benchmarking Deepfake Detectors Against Moiré-Induced Distortions
---

# Through the Lens: Benchmarking Deepfake Detectors Against Moiré-Induced Distortions
**arXiv**：[2510.23225v1](https://arxiv.org/abs/2510.23225) · [PDF](https://arxiv.org/pdf/2510.23225.pdf)  
**作者**：Razaib Tariq, Minji Heo, Simon S. Woo, Shahroz Tariq  

**一句话要点**：评估深度伪造检测器在莫尔纹失真下的性能，揭示其显著下降并提出DMF数据集。

**关键词**：深度伪造检测, 莫尔纹失真, 数据集构建, 性能评估, 真实世界挑战

## 3 点简述
- 核心问题：智能手机拍摄数字屏幕引入莫尔纹，导致深度伪造检测性能下降。
- 方法要点：使用真实和合成莫尔纹数据集，系统评估15种先进检测器。
- 实验或效果：莫尔纹使检测准确率下降达25.4%，去莫尔纹方法反而恶化问题。

## 摘要（原文）

> Deepfake detection remains a pressing challenge, particularly in real-world
> settings where smartphone-captured media from digital screens often introduces
> Moir\'e artifacts that can distort detection outcomes. This study
> systematically evaluates state-of-the-art (SOTA) deepfake detectors on
> Moir\'e-affected videos, an issue that has received little attention. We
> collected a dataset of 12,832 videos, spanning 35.64 hours, from the Celeb-DF,
> DFD, DFDC, UADFV, and FF++ datasets, capturing footage under diverse real-world
> conditions, including varying screens, smartphones, lighting setups, and camera
> angles. To further examine the influence of Moir\'e patterns on deepfake
> detection, we conducted additional experiments using our DeepMoir\'eFake,
> referred to as (DMF) dataset and two synthetic Moir\'e generation techniques.
> Across 15 top-performing detectors, our results show that Moir\'e artifacts
> degrade performance by as much as 25.4%, while synthetically generated Moir\'e
> patterns lead to a 21.4% drop in accuracy. Surprisingly, demoir\'eing methods,
> intended as a mitigation approach, instead worsened the problem, reducing
> accuracy by up to 17.2%. These findings underscore the urgent need for
> detection models that can robustly handle Moir\'e distortions alongside other
> realworld challenges, such as compression, sharpening, and blurring. By
> introducing the DMF dataset, we aim to drive future research toward closing the
> gap between controlled experiments and practical deepfake detection.

