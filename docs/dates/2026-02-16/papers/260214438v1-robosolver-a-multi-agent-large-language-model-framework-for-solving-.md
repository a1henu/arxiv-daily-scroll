---
layout: default
title: RoboSolver: A Multi-Agent Large Language Model Framework for Solving Robotic Arm Problems
---

# RoboSolver: A Multi-Agent Large Language Model Framework for Solving Robotic Arm Problems
**arXiv**：[2602.14438v1](https://arxiv.org/abs/2602.14438) · [PDF](https://arxiv.org/pdf/2602.14438.pdf)  
**作者**：Hamid Khabazi, Ali F. Meghdari, Alireza Taheri  

**一句话要点**：提出基于LLM和VLM的多智能体框架RoboSolver，以自动解决机器人臂问题。

**关键词**：多智能体框架, 机器人臂问题, 大语言模型, 视觉语言模型, 运动学计算, 仿真控制

## 3 点简述
- 核心问题：如何自动分析和解决机器人操纵器的运动学与控制问题。
- 方法要点：集成LLM和VLM，支持文本与视觉输入，自动执行运动学计算、仿真和控制。
- 实验或效果：在三个基准测试中，框架集成GPT-4o时准确率达0.97，显著优于原始模型。

## 摘要（原文）

> This study proposes an intelligent multi-agent framework built on LLMs and VLMs and specifically tailored to robotics. The goal is to integrate the strengths of LLMs and VLMs with computational tools to automatically analyze and solve problems related to robotic manipulators. Our developed framework accepts both textual and visual inputs and can automatically perform forward and inverse kinematics, compute velocities and accelerations of key points, generate 3D simulations of the robot, and ultimately execute motion control within the simulated environment, all according to the user's query. To evaluate the framework, three benchmark tests were designed, each consisting of ten questions. In the first benchmark test, the framework was evaluated while connected to GPT-4o, DeepSeek-V3.2, and Claude-Sonnet-4.5, as well as their corresponding raw models. The objective was to extract the forward kinematics of robots directly from textual descriptions. The results showed that the framework integrated with GPT-4o achieved the highest accuracy, reaching 0.97 in computing the final solution, whereas the raw model alone attained an accuracy of only 0.30 for the same task. Similarly, for the other two models, the framework consistently outperformed the corresponding raw models in terms of accuracy. The second benchmark test was identical to the first, except that the input was provided in visual form. In this test, the GPT-4o LLM was used alongside the Gemini 2.5 Pro VLM. The results showed that the framework achieved an accuracy of 0.93 in obtaining the final answer, which is approximately 20% higher than that of the corresponding raw model. The third benchmark test encompassed a range of robotic tasks, including simulation, control, velocity and acceleration computation, as well as inverse kinematics and Jacobian calculation, for which the framework achieved an accuracy of 0.97.

