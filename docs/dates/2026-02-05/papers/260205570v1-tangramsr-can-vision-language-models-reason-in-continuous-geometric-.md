---
layout: default
title: TangramSR: Can Vision-Language Models Reason in Continuous Geometric Space?
---

# TangramSR: Can Vision-Language Models Reason in Continuous Geometric Space?
**arXiv**：[2602.05570v1](https://arxiv.org/abs/2602.05570) · [PDF](https://arxiv.org/pdf/2602.05570.pdf)  
**作者**：Yikun Zong, Cheston Tan  

**一句话要点**：提出测试时自精炼框架，通过上下文学习与奖励反馈增强视觉语言模型的连续几何推理能力。

**关键词**：视觉语言模型, 几何推理, 测试时自精炼, 上下文学习, 奖励反馈, Tangram拼图

## 3 点简述
- 核心问题：视觉语言模型在连续几何推理中表现不佳，如Tangram拼图任务IoU远低于人类。
- 方法要点：设计无需参数更新的测试时自精炼框架，结合上下文学习和奖励引导反馈循环。
- 实验或效果：在中等三角形案例中，IoU从0.63提升至0.932，显著改善几何推理性能。

## 摘要（原文）

> Humans excel at spatial reasoning tasks like Tangram puzzle assembly through cognitive processes involving mental rotation, iterative refinement, and visual feedback. Inspired by how humans solve Tangram puzzles through trial-and-error, observation, and correction, we design a framework that models these human cognitive mechanisms. However, comprehensive experiments across five representative Vision-Language Models (VLMs) reveal systematic failures in continuous geometric reasoning: average IoU of only 0.41 on single-piece tasks, dropping to 0.23 on two-piece composition, far below human performance where children can complete Tangram tasks successfully. This paper addresses a fundamental challenge in self-improving AI: can models iteratively refine their predictions at test time without parameter updates? We introduce a test-time self-refinement framework that combines in-context learning (ICL) with reward-guided feedback loops, inspired by human cognitive processes. Our training-free verifier-refiner agent applies recursive refinement loops that iteratively self-refine predictions based on geometric consistency feedback, achieving IoU improvements from 0.63 to 0.932 on medium-triangle cases without any model retraining. This demonstrates that incorporating human-inspired iterative refinement mechanisms through ICL and reward loops can substantially enhance geometric reasoning in VLMs, moving self-improving AI from promise to practice in continuous spatial domains. Our work is available at this anonymous link https://anonymous.4open.science/r/TangramVLM-F582/.

