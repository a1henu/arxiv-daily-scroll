---
layout: default
title: Incremental Validation of Automated Driving Functions using Generic Volumes in Micro- Operational Design Domains
---

# Incremental Validation of Automated Driving Functions using Generic Volumes in Micro- Operational Design Domains
**arXiv**：[2512.11351v1](https://arxiv.org/abs/2512.11351) · [PDF](https://arxiv.org/pdf/2512.11351.pdf)  
**作者**：Steffen Schäfer, Martin Cichon  

**一句话要点**：提出基于微操作设计域和通用立方体的结构化方法，以系统验证自动驾驶感知功能。

**关键词**：自动驾驶验证, 微操作设计域, 场景测试, 感知评估, 闭环仿真, 安全论证

## 3 点简述
- 核心问题：从操作设计域到具体测试用例的转换过程缺乏结构化，完整性难以保证。
- 方法要点：将操作设计域细分为微操作设计域，使用通用立方体抽象表示障碍物生成测试用例。
- 实验或效果：在闭环协同仿真环境中测试，以碰撞与安全停止为指标，系统探索感知边缘案例。

## 摘要（原文）

> The validation of highly automated, perception-based driving systems must ensure that they function correctly under the full range of real-world conditions. Scenario-based testing is a prominent approach to addressing this challenge, as it involves the systematic simulation of objects and environments. Operational Design Domains (ODDs) are usually described using a taxonomy of qualitative designations for individual objects. However, the process of transitioning from taxonomy to concrete test cases remains unstructured, and completeness is theoretical. This paper introduces a structured method of subdividing the ODD into manageable sections, termed micro-ODDs (mODDs), and deriving test cases with abstract object representations. This concept is demonstrated using a one-dimensional, laterally guided manoeuvre involving a shunting locomotive within a constrained ODD. In this example, mODDs are defined and refined into narrow taxonomies that enable test case generation. Obstacles are represented as generic cubes of varying sizes, providing a simplified yet robust means of evaluating perception performance. A series of tests were conducted in a closed-loop, co-simulated virtual environment featuring photorealistic rendering and simulated LiDAR, GNSS and camera sensors. The results demonstrate how edge cases in obstacle detection can be systematically explored and how perception quality can be evaluated based on observed vehicle behaviour, using crash versus safe stop as the outcome metrics. These findings support the development of a standardised framework for safety argumentation and offer a practical step towards the validation and authorisation of automated driving functions.

