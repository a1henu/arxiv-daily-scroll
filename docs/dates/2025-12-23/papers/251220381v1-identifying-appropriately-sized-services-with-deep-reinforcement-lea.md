---
layout: default
title: Identifying Appropriately-Sized Services with Deep Reinforcement Learning
---

# Identifying Appropriately-Sized Services with Deep Reinforcement Learning
**arXiv**：[2512.20381v1](https://arxiv.org/abs/2512.20381) · [PDF](https://arxiv.org/pdf/2512.20381.pdf)  
**作者**：Syeda Tasnim Fabiha, Saad Shafiq, Wesley Klewerton Guez Assunção, Nenad Medvidović  

**一句话要点**：提出基于深度强化学习的Rake技术，从实现工件中识别适当规模的服务以解决服务分解挑战。

**关键词**：服务分解, 深度强化学习, 模块化质量, 业务能力对齐, 遗留系统现代化

## 3 点简述
- 核心问题：服务架构中定义适当规模服务困难，现有方法依赖文档或先验知识，不适用于现实场景。
- 方法要点：Rake利用深度强化学习，从源代码和文档直接分解服务，无需特定文档或人员访问，支持可定制目标函数。
- 实验或效果：在四个开源遗留项目上测试，Rake平均提升模块化质量7-14%，业务能力对齐18-22%，优于现有技术。

## 摘要（原文）

> Service-based architecture (SBA) has gained attention in industry and academia as a means to modernize legacy systems. It refers to a design style that enables systems to be developed as suites of small, loosely coupled, and autonomous components (services) that encapsulate functionality and communicate via language-agnostic APIs. However, defining appropriately sized services that capture cohesive subsets of system functionality remains challenging. Existing work often relies on the availability of documentation, access to project personnel, or a priori knowledge of the target number of services, assumptions that do not hold in many real-world scenarios. Our work addresses these limitations using a deep reinforcement learning-based approach to identify appropriately sized services directly from implementation artifacts. We present Rake, a reinforcement learning-based technique that leverages available system documentation and source code to guide service decomposition at the level of implementation methods. Rake does not require specific documentation or access to project personnel and is language-agnostic. It also supports a customizable objective function that balances modularization quality and business capability alignment, i.e., the degree to which a service covers the targeted business capability. We applied Rake to four open-source legacy projects and compared it with two state-of-the-art techniques. On average, Rake achieved 7-14 percent higher modularization quality and 18-22 percent stronger business capability alignment. Our results further show that optimizing solely for business context can degrade decomposition quality in tightly coupled systems, highlighting the need for balanced objectives.

