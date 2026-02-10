---
layout: default
title: Gesture Matters: Pedestrian Gesture Recognition for AVs Through Skeleton Pose Evaluation
---

# Gesture Matters: Pedestrian Gesture Recognition for AVs Through Skeleton Pose Evaluation
**arXiv**：[2602.08479v1](https://arxiv.org/abs/2602.08479) · [PDF](https://arxiv.org/pdf/2602.08479.pdf)  
**作者**：Alif Rizqullah Mahdi, Mahdi Rezaei, Natasha Merat  

**一句话要点**：提出基于骨架姿态评估的行人手势识别框架，以提升自动驾驶车辆对非语言交通交互的理解能力。

**关键词**：手势识别, 自动驾驶, 骨架姿态估计, 行人行为分析, 特征提取

## 3 点简述
- 核心问题：自动驾驶车辆难以解读行人在交通中的非语言手势，影响交互安全。
- 方法要点：使用2D姿态估计从WIVW数据集提取76个静态和动态特征，分类为停止、通行、感谢问候和无手势四类。
- 实验或效果：通过手部位置和移动速度等特征，在真实视频序列上实现87%的分类准确率。

## 摘要（原文）

> Gestures are a key component of non-verbal communication in traffic, often helping pedestrian-to-driver interactions when formal traffic rules may be insufficient. This problem becomes more apparent when autonomous vehicles (AVs) struggle to interpret such gestures. In this study, we present a gesture classification framework using 2D pose estimation applied to real-world video sequences from the WIVW dataset. We categorise gestures into four primary classes (Stop, Go, Thank & Greet, and No Gesture) and extract 76 static and dynamic features from normalised keypoints. Our analysis demonstrates that hand position and movement velocity are especially discriminative in distinguishing between gesture classes, achieving a classification accuracy score of 87%. These findings not only improve the perceptual capabilities of AV systems but also contribute to the broader understanding of pedestrian behaviour in traffic contexts.

