---
layout: default
title: Exp-Force: Experience-Conditioned Pre-Grasp Force Selection with Vision-Language Models
---

# Exp-Force: Experience-Conditioned Pre-Grasp Force Selection with Vision-Language Models
**arXiv**：[2603.08668v1](https://arxiv.org/abs/2603.08668) · [PDF](https://arxiv.org/pdf/2603.08668.pdf)  
**作者**：Siqi Shang, Minchao Huang, Bill Fan, Lillian Chin  

**一句话要点**：提出Exp-Force框架，基于视觉语言模型和先验经验预测最小可行抓取力，以解决柔性夹爪预抓取力选择难题。

**关键词**：预抓取力选择, 视觉语言模型, 经验条件推理, 柔性夹爪, 机器人抓取, 上下文学习

## 3 点简述
- 核心问题：柔性夹爪预抓取力选择困难，力过小需调整，力过大易损坏物体，且接触力学难以建模。
- 方法要点：从单张RGB图像检索相关先验抓取经验，利用视觉语言模型进行上下文推理，无需解析模型或手动启发式。
- 实验或效果：在129个物体实例上，最佳MAE为0.43 N，误差比零样本推理降低72%；真实世界测试中，合适力选择率从63%提升至87%。

## 摘要（原文）

> Accurate pre-contact grasp force selection is critical for safe and reliable robotic manipulation. Adaptive controllers regulate force after contact but still require a reasonable initial estimate. Starting a grasp with too little force requires reactive adjustment, while starting a grasp with too high a force risks damaging fragile objects. This trade-off is particularly challenging for compliant grippers, whose contact mechanics are difficult to model analytically. We propose Exp-Force, an experience-conditioned framework that predicts the minimum feasible grasping force from a single RGB image. The method retrieves a small set of relevant prior grasping experiences and conditions a vision-language model on these examples for in-context inference, without analytic contact models or manually designed heuristics. On 129 object instances, ExpForce achieves a best-case MAE of 0.43 N, reducing error by 72% over zero-shot inference. In real-world tests on 30 unseen objects, it improves appropriate force selection rate from 63% to 87%. These results demonstrate that Exp-Force enables reliable and generalizable pre-grasp force selection by leveraging prior interaction experiences. http://expforcesubmission.github.io/Exp-Force-Website/

