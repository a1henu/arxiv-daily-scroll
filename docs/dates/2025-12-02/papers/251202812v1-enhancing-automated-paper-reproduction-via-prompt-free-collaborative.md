---
layout: default
title: Enhancing Automated Paper Reproduction via Prompt-Free Collaborative Agents
---

# Enhancing Automated Paper Reproduction via Prompt-Free Collaborative Agents
**arXiv**：[2512.02812v1](https://arxiv.org/abs/2512.02812) · [PDF](https://arxiv.org/pdf/2512.02812.pdf)  
**作者**：Zijie Lin, Qilin Cai, Liang Shen, Mingjun Xiao  

**一句话要点**：提出无提示协作代理框架以增强自动化论文复现的代码生成质量

**关键词**：自动化论文复现, 协作代理, 代码生成, 无提示精炼, 验证机制

## 3 点简述
- 现有自动化论文复现框架缺乏步骤输出验证与精炼机制，依赖人工提示限制适应性
- 采用验证代理和精炼代理协作，基于原始系统提示自动检查并改进生成代码
- 在PaperBench Code-Dev和Paper2CodeBench数据集上实验，代码准确性和完整性提升约15%和13%

## 摘要（原文）

> Automated paper reproduction has emerged as a promising approach to accelerate scientific research, employing multi-step workflow frameworks to systematically convert academic papers into executable code. However, existing frameworks often lack mechanisms to verify and refine the outputs at each generation step, or rely heavily on manually designed prompts for self-refinement, which limits their adaptability and scalability. To address these limitations, we propose a prompt-free collaborative agent framework that automatically enhances the quality of paper-to-code generation. Our approach employs two collaborative agents: a verification agent that examines whether the outputs at each step satisfy the requirements specified in the corresponding system prompt, and a refinement agent that revises the outputs based on the identified issues. Unlike previous methods that require human experts to craft specific refinement prompts for each step, our framework achieves automatic verification and improvement by leveraging only the original system prompts. We integrate our collaborative agents into the Paper2Code framework and conduct comprehensive experiments on PaperBench Code-Dev and Paper2CodeBench datasets. Experimental results demonstrate that our approach significantly improves the accuracy and completeness of reproduced code, achieving performance gains of approximately 15\% and 13\%, respectively, compared to the baseline without our agents. Furthermore, comparative experiments against Self-Refine validate the robustness and consistency of our prompt-free approach across different datasets.

