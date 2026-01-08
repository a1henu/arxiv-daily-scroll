---
layout: default
title: From Score to Sound: An End-to-End MIDI-to-Motion Pipeline for Robotic Cello Performance
---

# From Score to Sound: An End-to-End MIDI-to-Motion Pipeline for Robotic Cello Performance
**arXiv**：[2601.03562v1](https://arxiv.org/abs/2601.03562) · [PDF](https://arxiv.org/pdf/2601.03562.pdf)  
**作者**：Samantha Sudhoff, Pranesh Velmurugan, Jiashu Liu, Vincent Zhao, Yung-Hsiang Lu, Kristen Yeon-Ji Yun  

**一句话要点**：提出端到端MIDI到运动管道，实现机器人无动捕大提琴演奏

**关键词**：机器人演奏, 端到端管道, MIDI到运动, 碰撞感知, 音乐图灵测试, 强化学习

## 3 点简述
- 核心问题：机器人演奏弦乐器需精确控制弓角度和压力，现有方法依赖昂贵动捕且无法视奏
- 方法要点：利用UR5e机器人Freedrive功能，直接从MIDI乐谱生成碰撞感知的弓运动，无需动捕
- 实验或效果：通过音乐图灵测试评估，132名参与者对比人类基准，并发布首个机器人演奏数据集

## 摘要（原文）

> Robot musicians require precise control to obtain proper note accuracy, sound quality, and musical expression. Performance of string instruments, such as violin and cello, presents a significant challenge due to the precise control required over bow angle and pressure to produce the desired sound. While prior robotic cellists focus on accurate bowing trajectories, these works often rely on expensive motion capture techniques, and fail to sightread music in a human-like way.
>   We propose a novel end-to-end MIDI score to robotic motion pipeline which converts musical input directly into collision-aware bowing motions for a UR5e robot cellist. Through use of Universal Robot Freedrive feature, our robotic musician can achieve human-like sound without the need for motion capture. Additionally, this work records live joint data via Real-Time Data Exchange (RTDE) as the robot plays, providing labeled robotic playing data from a collection of five standard pieces to the research community. To demonstrate the effectiveness of our method in comparison to human performers, we introduce the Musical Turing Test, in which a collection of 132 human participants evaluate our robot's performance against a human baseline. Human reference recordings are also released, enabling direct comparison for future studies. This evaluation technique establishes the first benchmark for robotic cello performance. Finally, we outline a residual reinforcement learning methodology to improve upon baseline robotic controls, highlighting future opportunities for improved string-crossing efficiency and sound quality.

