---
layout: default
title: Evolving Medical Imaging Agents via Experience-driven Self-skill Discovery
---

# Evolving Medical Imaging Agents via Experience-driven Self-skill Discovery
**arXiv**：[2603.05860v1](https://arxiv.org/abs/2603.05860) · [PDF](https://arxiv.org/pdf/2603.05860.pdf)  
**作者**：Lin Fan, Pengyu Dai, Zhipeng Deng, Haolin Wang, Xun Gong, Yefeng Zheng, Yafei Ou  

**一句话要点**：提出MACRO自进化医疗代理，通过经验驱动工具发现解决静态工具链在医疗影像中的脆弱性问题

**关键词**：医疗影像代理, 自进化系统, 工具发现, 经验增强, 多步编排, 跨域泛化

## 3 点简述
- 核心问题：现有LLM代理在医疗影像中工具集和调用策略静态，难以适应领域变化和任务演进
- 方法要点：从执行轨迹自主识别有效多步工具序列，合成可复用复合工具，并基于图像特征记忆和强化训练实现闭环自改进
- 实验或效果：在多样化医疗影像数据集上，自主复合工具发现提升多步编排准确性和跨域泛化能力

## 摘要（原文）

> Clinical image interpretation is inherently multi-step and tool-centric: clinicians iteratively combine visual evidence with patient context, quantify findings, and refine their decisions through a sequence of specialized procedures. While LLM-based agents promise to orchestrate such heterogeneous medical tools, existing systems treat tool sets and invocation strategies as static after deployment. This design is brittle under real-world domain shifts, across tasks, and evolving diagnostic requirements, where predefined tool chains frequently degrade and demand costly manual re-design. We propose MACRO, a self-evolving, experience-augmented medical agent that shifts from static tool composition to experience-driven tool discovery. From verified execution trajectories, the agent autonomously identifies recurring effective multi-step tool sequences, synthesizes them into reusable composite tools, and registers these as new high-level primitives that continuously expand its behavioral repertoire. A lightweight image-feature memory grounds tool selection in a visual-clinical context, while a GRPO-like training loop reinforces reliable invocation of discovered composites, enabling closed-loop self-improvement with minimal supervision. Extensive experiments across diverse medical imaging datasets and tasks demonstrate that autonomous composite tool discovery consistently improves multi-step orchestration accuracy and cross-domain generalization over strong baselines and recent state-of-the-art agentic methods, bridging the gap between brittle static tool use and adaptive, context-aware clinical AI assistance. Code will be available upon acceptance.

