
### Design.md

```markdown
# Code Review Agent 设计文档

## 1. 项目目标

本项目目标是实现一个简单的代码审查 Agent。

Agent 可以根据用户输入自动读取代码文件，并利用大语言模型分析代码功能、潜在 Bug 和改进建议。

项目重点体现 Agent 的基本设计模式：

输入 → 推理 → 工具调用 → 输出

## 2. 系统架构

系统主要由四部分组成：

1. 用户交互层
2. Agent 核心层
3. Tool 工具层
4. LLM 服务层

系统架构：

```text
          User
           |
           v
     CodeAgent.py
           |
           v
        Agent
       /     \
      v       v
 File Tool    LLM
      \       /
       \     /
        v   v
        Answer