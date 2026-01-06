---
layout: default
title: Learning Diffusion Policy from Primitive Skills for Robot Manipulation
---

# Learning Diffusion Policy from Primitive Skills for Robot Manipulation
**arXiv**：[2601.01948v1](https://arxiv.org/abs/2601.01948) · [PDF](https://arxiv.org/pdf/2601.01948.pdf)  
**作者**：Zhihao Gu, Ming Yang, Difan Zou, Dong Xu  

**一句话要点**：提出技能条件扩散策略SDP，通过分解任务为原始技能以提升机器人操作性能。

**关键词**：扩散策略, 机器人操作, 技能学习, 视觉语言模型, 动作规划

## 3 点简述
- 现有扩散策略依赖全局指令，可能导致动作生成错位。
- SDP集成可解释技能学习与条件动作规划，使用视觉语言模型提取离散表示。
- 在仿真基准和真实机器人部署中，SDP一致优于现有方法。

## 摘要（原文）

> Diffusion policies (DP) have recently shown great promise for generating actions in robotic manipulation. However, existing approaches often rely on global instructions to produce short-term control signals, which can result in misalignment in action generation. We conjecture that the primitive skills, referred to as fine-grained, short-horizon manipulations, such as ``move up'' and ``open the gripper'', provide a more intuitive and effective interface for robot learning. To bridge this gap, we propose SDP, a skill-conditioned DP that integrates interpretable skill learning with conditional action planning. SDP abstracts eight reusable primitive skills across tasks and employs a vision-language model to extract discrete representations from visual observations and language instructions. Based on them, a lightweight router network is designed to assign a desired primitive skill for each state, which helps construct a single-skill policy to generate skill-aligned actions. By decomposing complex tasks into a sequence of primitive skills and selecting a single-skill policy, SDP ensures skill-consistent behavior across diverse tasks. Extensive experiments on two challenging simulation benchmarks and real-world robot deployments demonstrate that SDP consistently outperforms SOTA methods, providing a new paradigm for skill-based robot learning with diffusion policies.

