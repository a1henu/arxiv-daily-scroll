---
layout: default
title: BEAP-Agent: Backtrackable Execution and Adaptive Planning for GUI Agents
---

# BEAP-Agent: Backtrackable Execution and Adaptive Planning for GUI Agents
**arXiv**：[2601.21352v1](https://arxiv.org/abs/2601.21352) · [PDF](https://arxiv.org/pdf/2601.21352.pdf)  
**作者**：Ziyu Lu, Tengjin Weng, Yiying Yang, Yuhang Zhao, Xinxin Huang, Wenhao Jiang  

**一句话要点**：提出BEAP-Agent框架，通过回溯执行与自适应规划解决GUI代理任务失败问题

**关键词**：GUI代理, 回溯执行, 自适应规划, 任务探索, DFS框架

## 3 点简述
- 核心问题：现有GUI代理在错误探索路径后难以恢复，导致任务失败
- 方法要点：基于DFS建模任务执行，支持长距离多级状态回溯与动态任务跟踪
- 实验或效果：在OSWorld基准测试中达到28.2%准确率，验证方法有效性

## 摘要（原文）

> GUI agents are designed to automate repetitive tasks and enhance productivity. However, existing GUI agents struggle to recover once they follow an incorrect exploration path, often leading to task failure. In this work, we model GUI task execution as a DFS process and propose BEAP-Agent, a DFS-based framework that supports long-range, multi-level state backtracking with dynamic task tracking and updating. The framework consists of three collaborative components: Planner, Executor, and Tracker. Together, they enable effective task exploration and execution. BEAP-Agent fills the gap in systematic backtracking mechanisms for GUI agents, offering a systematic solution for long-horizon task exploration. We conducted a systematic evaluation on the OSWorld benchmark, where BEAP-Agent achieved an accuracy of 28.2%, validating the effectiveness of the proposed method.

