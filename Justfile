#
# USAGE:
#   just
#

#
# CONFIG
#
PYTHON_VERSION := "3.14"
VENV_DIR := ".venv"

RUFF := "ruff"
RUFF_FLAGS := "--line-length 120"
TY := "ty"
UV := "uv"
UV_FORMAT_FLAGS := "--preview-features format"

default: healthy


#
# TASKS
#

#
# UV tasks
#
uv-install:
    curl -LsSf https://astral.sh/uv/install.sh | sh


uv-sync:
    {{UV}} sync


uv-update:
    {{UV}} self update


#
# LINT tasks
#
lint: ruff-check

ruff-install:
    {{UV}} tool install {{RUFF}}

ruff-check:
    @{{RUFF}} check . {{RUFF_FLAGS}} --exit-zero
    @echo "✅ Lint passed!"
    @echo



#
# FORMAT tasks
#
format:
    @{{UV}} format {{UV_FORMAT_FLAGS}}

format-check:
    @{{UV}} format {{UV_FORMAT_FLAGS}} --check



#
# TYPECHECK tasks
#
typecheck:
    @{{TY}} check
    @echo "✅ Typecheck passed!"


#
# PROJECT LIFECYCLE tasks
#
clean:
    @echo "🧹 Removing virtual environment..."
    rm -rf {{VENV_DIR}}

init: uv-install uv-update virtualenv ruff-install
    @echo "✅ Project environment initialized!"

install:
    {{UV}} sync
    @echo "✅ Dependencies installed!"

virtualenv: uv-update
    @echo "🔧 Creating virtual environment with Python {{PYTHON_VERSION}}..."
    {{UV}} venv --python {{PYTHON_VERSION}} {{VENV_DIR}}
    @echo "✅ Virtualenv ready. Activate with: source {{VENV_DIR}}/bin/activate"


#
# FUNCTIONAL tasks
#
healthy:
    just format && \
    just lint && \
    just typecheck && \
    just test

sync:
    {{UV}} sync

test:
    pytest *test.py
    @echo "✅ Tests passed!"
    @echo
