---
layout: default
title: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning
---

# Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning
**arXiv**：[2511.14396v1](https://arxiv.org/abs/2511.14396) · [PDF](https://arxiv.org/pdf/2511.14396.pdf)  
**作者**：Xiuxiu Qi, Yu Yang, Jiannong Cao, Luyao Bai, Chongshan Fan, Chengtai Cao, Hongpeng Wang  

**一句话要点**：提出连续视觉-语言-动作协同学习框架以解决行为克隆中的语义-物理错位问题

**关键词**：行为克隆, 视觉-语言-动作协同学习, 语义-物理对齐, 机器人操作, 复合误差缓解

## 3 点简述
- 核心问题：行为克隆中序列动作决策的复合误差导致物理不连续和语义-物理错位
- 方法要点：通过双向跨注意力实现语义与视觉运动表示的锚定，确保连续协同学习
- 实验或效果：在模拟和真实机器人测试中平均提升8.0%，泛化性强

## 摘要（原文）

> Language-conditioned manipulation facilitates human-robot interaction via behavioral cloning (BC), which learns control policies from human demonstrations and serves as a cornerstone of embodied AI. Overcoming compounding errors in sequential action decisions remains a central challenge to improving BC performance. Existing approaches mitigate compounding errors through data augmentation, expressive representation, or temporal abstraction. However, they suffer from physical discontinuities and semantic-physical misalignment, leading to inaccurate action cloning and intermittent execution. In this paper, we present Continuous vision-language-action Co-Learning with Semantic-Physical Alignment (CCoL), a novel BC framework that ensures temporally consistent execution and fine-grained semantic grounding. It generates robust and smooth action execution trajectories through continuous co-learning across vision, language, and proprioceptive inputs (e.g., robot internal states). Meanwhile, we anchor language semantics to visuomotor representations by a bidirectional cross-attention to learn contextual information for action generation, successfully overcoming the problem of semantic-physical misalignment. Extensive experiments show that CCoL achieves an average 8.0% relative improvement across three simulation suites, with up to 19.2% relative gain in human-demonstrated bimanual insertion tasks. Real-world tests on a 7-DoF robot further confirm CCoL's generalization under unseen and noisy object states.

