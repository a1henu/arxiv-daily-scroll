---
layout: default
title: M3CoTBench: Benchmark Chain-of-Thought of MLLMs in Medical Image Understanding
---

# M3CoTBench: Benchmark Chain-of-Thought of MLLMs in Medical Image Understanding
**arXiv**：[2601.08758v1](https://arxiv.org/abs/2601.08758) · [PDF](https://arxiv.org/pdf/2601.08758.pdf)  
**作者**：Juntao Jiang, Jiangning Zhang, Yali Bi, Jinsheng Bai, Weixuan Liu, Weiwei Jin, Zhucun Xue, Yong Liu, Xiaobin Hu, Shuicheng Yan  

**一句话要点**：提出M3CoTBench基准以评估医疗图像理解中多模态大语言模型的思维链推理

**关键词**：医疗图像理解, 思维链推理, 多模态大语言模型, 基准评估, 临床诊断, 透明AI

## 3 点简述
- 当前医疗图像理解基准忽略推理路径，缺乏透明性，难以辅助诊断决策
- M3CoTBench包含多难度数据集、任务及针对临床推理的思维链评估指标
- 基准系统评估多个MLLMs，揭示其在生成可靠、临床可解释推理方面的局限性

## 摘要（原文）

> Chain-of-Thought (CoT) reasoning has proven effective in enhancing large language models by encouraging step-by-step intermediate reasoning, and recent advances have extended this paradigm to Multimodal Large Language Models (MLLMs). In the medical domain, where diagnostic decisions depend on nuanced visual cues and sequential reasoning, CoT aligns naturally with clinical thinking processes. However, Current benchmarks for medical image understanding generally focus on the final answer while ignoring the reasoning path. An opaque process lacks reliable bases for judgment, making it difficult to assist doctors in diagnosis. To address this gap, we introduce a new M3CoTBench benchmark specifically designed to evaluate the correctness, efficiency, impact, and consistency of CoT reasoning in medical image understanding. M3CoTBench features 1) a diverse, multi-level difficulty dataset covering 24 examination types, 2) 13 varying-difficulty tasks, 3) a suite of CoT-specific evaluation metrics (correctness, efficiency, impact, and consistency) tailored to clinical reasoning, and 4) a performance analysis of multiple MLLMs. M3CoTBench systematically evaluates CoT reasoning across diverse medical imaging tasks, revealing current limitations of MLLMs in generating reliable and clinically interpretable reasoning, and aims to foster the development of transparent, trustworthy, and diagnostically accurate AI systems for healthcare. Project page at https://juntaojianggavin.github.io/projects/M3CoTBench/.

