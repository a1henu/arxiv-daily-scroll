---
layout: default
title: RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation
---

# RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation
**arXiv**：[2510.23571v1](https://arxiv.org/abs/2510.23571) · [PDF](https://arxiv.org/pdf/2510.23571.pdf)  
**作者**：Yash Jangir, Yidi Zhang, Kashu Yamazaki, Chenyu Zhang, Kuan-Hsun Tu, Tsung-Wei Ke, Lei Ke, Yonatan Bisk, Katerina Fragkiadaki  

**一句话要点**：提出RobotArena ∞框架，通过真实到模拟转换实现可扩展机器人基准测试

**关键词**：机器人基准测试, 真实到模拟转换, 视觉语言模型, 可扩展评估, 人类反馈

## 3 点简述
- 核心问题：真实世界机器人策略测试受限，难以大规模、安全、可重复评估
- 方法要点：利用视觉语言模型和生成建模，自动将视频演示转换为模拟环境
- 实验或效果：结合自动评分和人类偏好，系统扰动测试策略鲁棒性

## 摘要（原文）

> The pursuit of robot generalists - instructable agents capable of performing
> diverse tasks across diverse environments - demands rigorous and scalable
> evaluation. Yet real-world testing of robot policies remains fundamentally
> constrained: it is labor-intensive, slow, unsafe at scale, and difficult to
> reproduce. Existing simulation benchmarks are similarly limited, as they train
> and test policies within the same synthetic domains and cannot assess models
> trained from real-world demonstrations or alternative simulation environments.
> As policies expand in scope and complexity, these barriers only intensify,
> since defining "success" in robotics often hinges on nuanced human judgments of
> execution quality. In this paper, we introduce a new benchmarking framework
> that overcomes these challenges by shifting VLA evaluation into large-scale
> simulated environments augmented with online human feedback. Leveraging
> advances in vision-language models, 2D-to-3D generative modeling, and
> differentiable rendering, our approach automatically converts video
> demonstrations from widely used robot datasets into simulated counterparts.
> Within these digital twins, we assess VLA policies using both automated
> VLM-guided scoring and scalable human preference judgments collected from
> crowdworkers, transforming human involvement from tedious scene setup,
> resetting, and safety supervision into lightweight preference comparisons. To
> measure robustness, we systematically perturb simulated environments along
> multiple axes, such as textures and object placements, stress-testing policy
> generalization under controlled variation. The result is a continuously
> evolving, reproducible, and scalable benchmark for real-world trained robot
> manipulation policies, addressing a critical missing capability in today's
> robotics landscape.

