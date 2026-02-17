---
layout: default
title: Morphing of and writing with a scissor linkage mechanism
---

# Morphing of and writing with a scissor linkage mechanism
**arXiv**：[2602.14958v1](https://arxiv.org/abs/2602.14958) · [PDF](https://arxiv.org/pdf/2602.14958.pdf)  
**作者**：Mohanraj A, S Ganga Prasath  

**一句话要点**：提出基于剪刀连杆机构的形状变形与书写方法，通过优化框架实现自动化导航与检测。

**关键词**：剪刀连杆机构, 运动学分析, 形状变形, 优化框架, 自动化导航, 实验验证

## 3 点简述
- 研究剪刀连杆机构的运动学，利用单自由度实现整体形状变化。
- 推导单元有效曲率和尖端轨迹表达式，作为形状变形和书写任务的基础。
- 通过优化和实验验证，展示机构在复杂领域应用的潜力，但编程与无反馈实施挑战未知。

## 摘要（原文）

> Kinematics of mechanisms is intricately coupled to their geometry and their utility often arises out of the ability to perform reproducible motion with fewer actuating degrees of freedom. In this article, we explore the assembly of scissor-units, each made of two rigid linear members connected by a pin joint. The assembly has a single degree of freedom, where actuating any single unit results in a shape change of the entire assembly. We derive expressions for the effective curvature of the unit and the trajectory of the mechanism's tip as a function of the geometric variables which we then use as the basis to program two tasks in the mechanism: shape morphing and writing. By phrasing these tasks as optimization problems and utilizing the differentiable simulation framework, we arrive at solutions that are then tested in table-top experiments. Our results show that the geometry of scissor assemblies can be leveraged for automated navigation and inspection in complex domains, in light of the optimization framework. However, we highlight that the challenges associated with rapid programming and error-free implementation in experiments without feedback still remain.

