---
layout: default
title: Seismology modeling agent: A smart assistant for geophysical researchers
---

# Seismology modeling agent: A smart assistant for geophysical researchers
**arXiv**：[2512.14429v1](https://arxiv.org/abs/2512.14429) · [PDF](https://arxiv.org/pdf/2512.14429.pdf)  
**作者**：Yukun Ren, Siwei Yu, Kai Chen, Jianwei Ma  

**一句话要点**：提出基于大语言模型的智能交互工作流，以降低SPECFEM地震波模拟软件的使用门槛。

**关键词**：地震波模拟, 大语言模型, 智能工作流, MCP协议, 计算地震学, 自动化研究

## 3 点简述
- 核心问题：传统SPECFEM工作流学习曲线陡峭，依赖复杂手动文件编辑和命令行操作。
- 方法要点：引入首个SPECFEM的MCP服务器套件，将模拟过程分解为代理可执行的工具，支持从文件驱动到意图驱动的对话交互。
- 实验或效果：通过多案例验证，工作流在自主和交互模式下无缝运行，结果与标准基线一致，降低入门障碍并增强可重复性。

## 摘要（原文）

> To address the steep learning curve and reliance on complex manual file editing and command-line operations in the traditional workflow of the mainstream open-source seismic wave simulation software SPECFEM, this paper proposes an intelligent, interactive workflow powered by Large Language Models (LLMs). We introduce the first Model Context Protocol (MCP) server suite for SPECFEM (supporting 2D, 3D Cartesian, and 3D Globe versions), which decomposes the entire simulation process into discrete, agent-executable tools spanning from parameter generation and mesh partitioning to solver execution and visualization. This approach enables a paradigm shift from file-driven to intent-driven conversational interactions. The framework supports both fully automated execution and human-in-the-loop collaboration, allowing researchers to guide simulation strategies in real time and retain scientific decision-making authority while significantly reducing tedious low-level operations. Validated through multiple case studies, the workflow operates seamlessly in both autonomous and interactive modes, yielding high-fidelity results consistent with standard baselines. As the first application of MCP technology to computational seismology, this study significantly lowers the entry barrier, enhances reproducibility, and offers a promising avenue for advancing computational geophysics toward AI-assisted and automated scientific research. The complete source code is available at https://github.com/RenYukun1563/specfem-mcp.

