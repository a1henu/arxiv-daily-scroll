---
layout: default
title: Replanning Human-Robot Collaborative Tasks with Vision-Language Models via Semantic and Physical Dual-Correction
---

# Replanning Human-Robot Collaborative Tasks with Vision-Language Models via Semantic and Physical Dual-Correction
**arXiv**：[2602.14551v1](https://arxiv.org/abs/2602.14551) · [PDF](https://arxiv.org/pdf/2602.14551.pdf)  
**作者**：Taichi Kato, Takuya Kiyokawa, Namiko Saito, Kensuke Harada  

**一句话要点**：提出基于视觉语言模型的双重校正框架，以解决人机协作中指令模糊和物理执行失败问题。

**关键词**：人机协作, 视觉语言模型, 双重校正, 交互式重规划, 物理执行验证

## 3 点简述
- 核心问题：人机协作中人类指令常模糊，导致机器人行为难以物理可行和协同。
- 方法要点：通过内部校正验证逻辑一致性和任务可行性，外部校正检测并纠正物理执行失败。
- 实验或效果：仿真和真实世界实验显示，该方法提高成功率，支持交互式重规划。

## 摘要（原文）

> Human-Robot Collaboration (HRC) plays an important role in assembly tasks by enabling robots to plan and adjust their motions based on interactive, real-time human instructions. However, such instructions are often linguistically ambiguous and underspecified, making it difficult to generate physically feasible and cooperative robot behaviors. To address this challenge, many studies have applied Vision-Language Models (VLMs) to interpret high-level instructions and generate corresponding actions. Nevertheless, VLM-based approaches still suffer from hallucinated reasoning and an inability to anticipate physical execution failures. To address these challenges, we propose an HRC framework that augments a VLM-based reasoning with a dual-correction mechanism: an internal correction model that verifies logical consistency and task feasibility prior to action execution, and an external correction model that detects and rectifies physical failures through post-execution feedback. Simulation ablation studies demonstrate that the proposed method improves the success rate compared to baselines without correction models. Our real-world experiments in collaborative assembly tasks supported by object fixation or tool preparation by an upper body humanoid robot further confirm the framewor's effectiveness in enabling interactive replanning across different collaborative tasks in response to human instructions, validating its practical feasibility.

