---
layout: default
title: Team-Aware Football Player Tracking with SAM: An Appearance-Based Approach to Occlusion Recovery
---

# Team-Aware Football Player Tracking with SAM: An Appearance-Based Approach to Occlusion Recovery
**arXiv**：[2512.08467v1](https://arxiv.org/abs/2512.08467) · [PDF](https://arxiv.org/pdf/2512.08467.pdf)  
**作者**：Chamath Ranasinghe, Uthayasanker Thayasivam  

**一句话要点**：提出基于SAM的团队感知足球球员跟踪方法，结合外观模型以提升遮挡恢复能力。

**关键词**：足球球员跟踪, 遮挡恢复, SAM模型, 外观重识别, 团队感知, 实时处理

## 3 点简述
- 核心问题：足球球员跟踪面临频繁遮挡、外观相似和快速运动等挑战。
- 方法要点：结合SAM进行精确初始化，使用HSV直方图外观模型进行重识别以改进遮挡恢复。
- 实验效果：在足球视频序列中，轻遮挡下跟踪成功率100%，拥挤场景下90%，重遮挡恢复率50%。

## 摘要（原文）

> Football player tracking is challenged by frequent occlusions, similar appearances, and rapid motion in crowded scenes. This paper presents a lightweight SAM-based tracking method combining the Segment Anything Model (SAM) with CSRT trackers and jersey color-based appearance models. We propose a team-aware tracking system that uses SAM for precise initialization and HSV histogram-based re-identification to improve occlusion recovery. Our evaluation measures three dimensions: processing speed (FPS and memory), tracking accuracy (success rate and box stability), and robustness (occlusion recovery and identity consistency). Experiments on football video sequences show that the approach achieves 7.6-7.7 FPS with stable memory usage (~1880 MB), maintaining 100 percent tracking success in light occlusions and 90 percent in crowded penalty-box scenarios with 5 or more players. Appearance-based re-identification recovers 50 percent of heavy occlusions, demonstrating the value of domain-specific cues. Analysis reveals key trade-offs: the SAM + CSRT combination provides consistent performance across crowd densities but struggles with long-term occlusions where players leave the frame, achieving only 8.66 percent re-acquisition success. These results offer practical guidelines for deploying football tracking systems under resource constraints, showing that classical tracker-based methods work well with continuous visibility but require stronger re-identification mechanisms for extended absences.

