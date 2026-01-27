---
layout: default
title: AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security
---

# AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security
**arXiv**：[2601.18491v1](https://arxiv.org/abs/2601.18491) · [PDF](https://arxiv.org/pdf/2601.18491.pdf)  
**作者**：Dongrui Liu, Qihan Ren, Chen Qian, Shuai Shao, Yuejin Xie, Yu Li, Zhonghao Yang, Haoyu Luo, Peng Wang, Qingyu Liu, Binxin Hu, Ling Tang, Jilin Mei, Dadi Guo, Leitao Yuan, Junyao Yang, Guanxu Chen, Qihao Lin, Yi Yu, Bo Zhang, Jiaxuan Guo, Jie Zhang, Wenqi Shao, Huiqi Deng, Zhiheng Xi, Wenjie Wang, Wenxuan Wang, Wen Shen, Zhikai Chen, Haoyu Xie, Jialing Tao, Juntao Dai, Jiaming Ji, Zhongjie Ba, Linfeng Zhang, Yong Liu, Quanshi Zhang, Lei Zhu, Zhihua Wei, Hui Xue, Chaochao Lu, Jing Shao, Xia Hu  

**一句话要点**：提出AgentDoG诊断护栏框架以解决AI代理在自主工具使用和环境交互中的安全与安保挑战。

**关键词**：AI代理安全, 诊断护栏, 风险分类法, 细粒度监控, 代理对齐, 安全基准

## 3 点简述
- 核心问题：现有护栏模型缺乏代理风险意识和风险诊断透明度，无法覆盖复杂多样的风险行为。
- 方法要点：基于统一三维分类法（来源、失效模式、后果）构建细粒度代理安全基准ATBench和诊断护栏框架AgentDoG。
- 实验或效果：在多样复杂交互场景中实现最先进的代理安全调节性能，提供根因诊断和透明度，支持有效代理对齐。

## 摘要（原文）

> The rise of AI agents introduces complex safety and security challenges arising from autonomous tool use and environmental interactions. Current guardrail models lack agentic risk awareness and transparency in risk diagnosis. To introduce an agentic guardrail that covers complex and numerous risky behaviors, we first propose a unified three-dimensional taxonomy that orthogonally categorizes agentic risks by their source (where), failure mode (how), and consequence (what). Guided by this structured and hierarchical taxonomy, we introduce a new fine-grained agentic safety benchmark (ATBench) and a Diagnostic Guardrail framework for agent safety and security (AgentDoG). AgentDoG provides fine-grained and contextual monitoring across agent trajectories. More Crucially, AgentDoG can diagnose the root causes of unsafe actions and seemingly safe but unreasonable actions, offering provenance and transparency beyond binary labels to facilitate effective agent alignment. AgentDoG variants are available in three sizes (4B, 7B, and 8B parameters) across Qwen and Llama model families. Extensive experimental results demonstrate that AgentDoG achieves state-of-the-art performance in agentic safety moderation in diverse and complex interactive scenarios. All models and datasets are openly released.

